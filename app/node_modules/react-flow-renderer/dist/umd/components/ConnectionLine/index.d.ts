import { CSSProperties } from 'react';
import { ConnectionLineType, ConnectionLineComponent, HandleType } from '../../types';
interface ConnectionLineProps {
    connectionNodeId: string;
    connectionHandleId: string | null;
    connectionHandleType: HandleType;
    connectionPositionX: number;
    connectionPositionY: number;
    connectionLineType: ConnectionLineType;
    isConnectable: boolean;
    connectionLineStyle?: CSSProperties;
    CustomConnectionLineComponent?: ConnectionLineComponent;
}
declare const _default: ({ connectionNodeId, connectionHandleId, connectionHandleType, connectionLineStyle, connectionPositionX, connectionPositionY, connectionLineType, isConnectable, CustomConnectionLineComponent, }: ConnectionLineProps) => JSX.Element | null;
export default _default;
