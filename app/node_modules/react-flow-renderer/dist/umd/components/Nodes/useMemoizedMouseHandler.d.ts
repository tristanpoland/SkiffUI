import { MouseEvent } from 'react';
import { GetState } from 'zustand';
import { ReactFlowState, Node } from '../../types';
declare function useMemoizedMouseHandler(id: string, dragging: boolean, getState: GetState<ReactFlowState>, handler?: (event: MouseEvent, node: Node) => void): (event: MouseEvent) => void;
export default useMemoizedMouseHandler;
