import { Node } from './node';
export declare class Selected {
    list: Node[];
    add(item: Node, accumulate?: boolean): void;
    clear(): void;
    remove(item: Node): void;
    contains(item: Node): boolean;
    each(callback: (n: Node, index: number) => void): void;
}
