export namespace MetadataBackup.Response {
    export interface ExecutionResult<ResultType> {
        error: boolean;
        errorCode: number;
        errorMessage: string;
        response: ResultType;
        count: number;
    }

    export interface VideoMetadata {
        id: string;
        title: string;
        description: string;
        published: number;
        uploader: string;
        uploaderId: string;
        authentic: boolean;
    }

    export interface VideoAddResult {
        totalItemProcessed: number;
        totalNewItemsAdded: number;
        totalItemsFailedToAdd: number;
        addedVideoIds: string[];
        failedVideoIds: string[];
    }

    export interface VideoListResult {
        videos: VideoMetadata[],
        noRecord: string[]
    }
}
