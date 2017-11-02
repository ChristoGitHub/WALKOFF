import { ParameterApi } from './parameterApi';
import { ReturnApi } from './returnApi';

export class ActionApi {
	name: string;
	description: string;
	parameters: ParameterApi[] = [];
	returns: ReturnApi[] = [];
	// Name of event in the case of a triggered action, null or whitespace to indicate no event
	event: string;
	run: string;
	deprecated: boolean;
	// tags: Tag[] = [];
	summary: string;
	// externalDocs: ExternalDoc[] = [];
}