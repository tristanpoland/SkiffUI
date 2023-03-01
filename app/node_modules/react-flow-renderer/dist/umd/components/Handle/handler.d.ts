import { MouseEvent as ReactMouseEvent } from 'react';
import { SetState } from 'zustand';
import { OnConnect, OnConnectStart, OnConnectStop, OnConnectEnd, ConnectionMode, Connection, HandleType, ReactFlowState } from '../../types';
declare type ValidConnectionFunc = (connection: Connection) => boolean;
declare type Result = {
    elementBelow: Element | null;
    isValid: boolean;
    connection: Connection;
    isHoveringHandle: boolean;
};
export declare function checkElementBelowIsValid(event: MouseEvent, connectionMode: ConnectionMode, isTarget: boolean, nodeId: string, handleId: string | null, isValidConnection: ValidConnectionFunc, doc: Document | ShadowRoot): Result;
export declare function onMouseDown(event: ReactMouseEvent, handleId: string | null, nodeId: string, setState: SetState<ReactFlowState>, onConnect: OnConnect, isTarget: boolean, isValidConnection: ValidConnectionFunc, connectionMode: ConnectionMode, elementEdgeUpdaterType?: HandleType, onEdgeUpdateEnd?: (evt: MouseEvent) => void, onConnectStart?: OnConnectStart, onConnectStop?: OnConnectStop, onConnectEnd?: OnConnectEnd): void;
export {};
