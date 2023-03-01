import { NodeInternals, Edge } from '../types';
declare function useVisibleEdges(onlyRenderVisible: boolean, nodeInternals: NodeInternals): {
    edges: Edge<any>[];
    level: number;
    isMaxLevel: boolean;
}[];
export default useVisibleEdges;
