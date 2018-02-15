import argparse
import json
import logging.config
import os
import sys
import traceback
from os.path import isfile

from gevent import monkey
from gevent import pywsgi

import walkoff.config.paths as paths
import walkoff.config.config as config

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

from walkoff import __version__

logger = logging.getLogger('walkoff')


def setup_logger():
    log_config = None
    if isfile(paths.logging_config_path):
        try:
            with open(paths.logging_config_path, 'rt') as log_config_file:
                log_config = json.loads(log_config_file.read())
        except (IOError, OSError):
            print('Could not read logging JSON file {}'.format(paths.logging_config_path))
        except ValueError:
            print('Invalid JSON in logging config file')
    else:
        print('No logging config found')

    if log_config is not None:
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig()
        logger.info("Basic logging is being used")


def run(host, port):
    from walkoff.core.multiprocessedexecutor.multiprocessedexecutor import spawn_worker_processes
    setup_logger()
    print_banner()
    pids = spawn_worker_processes()
    monkey.patch_all()

    from walkoff.scripts.compose_api import compose_api
    compose_api()

    from walkoff.server import flaskserver
    flaskserver.running_context.controller.initialize_threading(pids=pids)
    # The order of these imports matter for initialization (should probably be fixed)

    import walkoff.case.database as case_database
    case_database.initialize()

    server = setup_server(flaskserver.app, host, port)
    server.serve_forever()


def print_banner():
    banner = '***** Running WALKOFF v.{} *****'.format(__version__)
    header_footer_banner = '*' * len(banner)
    logger.info(header_footer_banner)
    logger.info(banner)
    logger.info(header_footer_banner)


def setup_server(app, host, port):
    if isfile(paths.certificate_path) and isfile(paths.private_key_path):
        server = pywsgi.WSGIServer((host, port), application=app,
                                   keyfile=paths.private_key_path, certfile=paths.certificate_path)
        protocol = 'https'
    else:
        logger.warning('Cannot find certificates. Using HTTP')
        server = pywsgi.WSGIServer((host, port), application=app)
        protocol = 'http'

    logger.info('Listening on host {0}://{1}:{2}'.format(protocol, host, port))
    return server


def parse_args():
    parser = argparse.ArgumentParser(description='Script to the WALKOFF server')
    parser.add_argument('-v', '--version', help='Get the version of WALKOFF running', action='store_true')
    parser.add_argument('-p', '--port', help='port to run the server on')
    parser.add_argument('-H', '--host', help='host address to run the server on')

    args = parser.parse_args()
    if args.version:
        print(__version__)
        exit(0)

    return args


def convert_host_port(args):
    host = config.host if args.host is None else args.host
    port = config.port if args.port is None else args.port
    try:
        port = int(port)
    except ValueError:
        print('Invalid port {}. Port must be an integer!'.format(port))
        exit(1)
    return host, port


def main():
    args = parse_args()
    exit_code = 0
    try:
        config.initialize()
        run(*convert_host_port(args))
    except KeyboardInterrupt:
        logger.info('Caught KeyboardInterrupt!')
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exc()
        exit_code = 1
    finally:
        from walkoff.server import flaskserver

        flaskserver.running_context.controller.shutdown_pool()
        logger.info('Shutting down server')
        os._exit(exit_code)


if __name__ == "__main__":
    main()
