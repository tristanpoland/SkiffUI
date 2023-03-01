import { ReactNode } from 'react';
import { PanOnScrollMode, KeyCode, OnMove, OnMoveStart, OnMoveEnd } from '../../types';
interface ZoomPaneProps {
    selectionKeyPressed: boolean;
    elementsSelectable?: boolean;
    zoomOnScroll?: boolean;
    zoomOnPinch?: boolean;
    panOnScroll?: boolean;
    panOnScrollSpeed?: number;
    panOnScrollMode?: PanOnScrollMode;
    zoomOnDoubleClick?: boolean;
    panOnDrag?: boolean;
    defaultPosition?: [number, number];
    defaultZoom?: number;
    onMove?: OnMove;
    onMoveStart?: OnMoveStart;
    onMoveEnd?: OnMoveEnd;
    zoomActivationKeyCode?: KeyCode;
    preventScrolling?: boolean;
    children: ReactNode;
    noWheelClassName: string;
    noPanClassName: string;
}
declare const ZoomPane: ({ onMove, onMoveStart, onMoveEnd, zoomOnScroll, zoomOnPinch, panOnScroll, panOnScrollSpeed, panOnScrollMode, zoomOnDoubleClick, selectionKeyPressed, elementsSelectable, panOnDrag, defaultPosition, defaultZoom, zoomActivationKeyCode, preventScrolling, children, noWheelClassName, noPanClassName, }: ZoomPaneProps) => JSX.Element;
export default ZoomPane;
