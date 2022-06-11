export declare class Socket {
    name: string;
    data: unknown;
    compatible: Socket[];
    constructor(name: string, data?: {});
    combineWith(socket: Socket): void;
    compatibleWith(socket: Socket): boolean;
}
