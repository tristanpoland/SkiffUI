import { GetState } from 'zustand';
import { CoordinateExtent, Edge, EdgeSelectionChange, Node, NodeInternals, NodePositionChange, NodeSelectionChange, ReactFlowState, XYPosition, FitViewOptions } from '../types';
export declare function createNodeInternals(nodes: Node[], nodeInternals: NodeInternals): NodeInternals;
export declare function isParentSelected(node: Node, nodeInternals: NodeInternals): boolean;
declare type CreatePostionChangeParams = {
    node: Node;
    nodeExtent: CoordinateExtent;
    nodeInternals: NodeInternals;
    diff?: XYPosition;
    dragging?: boolean;
};
export declare function createPositionChange({ node, diff, dragging, nodeExtent, nodeInternals, }: CreatePostionChangeParams): NodePositionChange;
declare type InternalFitViewOptions = {
    initial?: boolean;
} & FitViewOptions;
export declare function fitView(get: GetState<ReactFlowState>, options?: InternalFitViewOptions): boolean;
export declare function handleControlledNodeSelectionChange(nodeChanges: NodeSelectionChange[], nodeInternals: NodeInternals): Map<string, Node<any>>;
export declare function handleControlledEdgeSelectionChange(edgeChanges: EdgeSelectionChange[], edges: Edge[]): Edge<any>[];
export {};
