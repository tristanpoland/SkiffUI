import { b as useStore, _ as _slicedToArray, l as getRectOfNodes, A as getBoundsofRects } from './index-fdcea71e.js';
import React__default, { memo } from 'react';
import cc from 'classcat';
import shallow from 'zustand/shallow';
import 'zustand';
import 'zustand/context';
import 'd3-zoom';

var MiniMapNode = function MiniMapNode(_ref) {
  var x = _ref.x,
      y = _ref.y,
      width = _ref.width,
      height = _ref.height,
      style = _ref.style,
      color = _ref.color,
      strokeColor = _ref.strokeColor,
      strokeWidth = _ref.strokeWidth,
      className = _ref.className,
      borderRadius = _ref.borderRadius,
      shapeRendering = _ref.shapeRendering;

  var _ref2 = style || {},
      background = _ref2.background,
      backgroundColor = _ref2.backgroundColor;

  var fill = color || background || backgroundColor;
  return /*#__PURE__*/React__default.createElement("rect", {
    className: cc(['react-flow__minimap-node', className]),
    x: x,
    y: y,
    rx: borderRadius,
    ry: borderRadius,
    width: width,
    height: height,
    fill: fill,
    stroke: strokeColor,
    strokeWidth: strokeWidth,
    shapeRendering: shapeRendering
  });
};

MiniMapNode.displayName = 'MiniMapNode';
var MiniMapNode$1 = /*#__PURE__*/memo(MiniMapNode);

var defaultWidth = 200;
var defaultHeight = 150;

var selector = function selector(s) {
  return {
    width: s.width,
    height: s.height,
    transform: s.transform,
    nodeInternals: s.nodeInternals
  };
};

var MiniMap = function MiniMap(_ref) {
  var style = _ref.style,
      className = _ref.className,
      _ref$nodeStrokeColor = _ref.nodeStrokeColor,
      nodeStrokeColor = _ref$nodeStrokeColor === void 0 ? '#555' : _ref$nodeStrokeColor,
      _ref$nodeColor = _ref.nodeColor,
      nodeColor = _ref$nodeColor === void 0 ? '#fff' : _ref$nodeColor,
      _ref$nodeClassName = _ref.nodeClassName,
      nodeClassName = _ref$nodeClassName === void 0 ? '' : _ref$nodeClassName,
      _ref$nodeBorderRadius = _ref.nodeBorderRadius,
      nodeBorderRadius = _ref$nodeBorderRadius === void 0 ? 5 : _ref$nodeBorderRadius,
      _ref$nodeStrokeWidth = _ref.nodeStrokeWidth,
      nodeStrokeWidth = _ref$nodeStrokeWidth === void 0 ? 2 : _ref$nodeStrokeWidth,
      _ref$maskColor = _ref.maskColor,
      maskColor = _ref$maskColor === void 0 ? 'rgb(240, 242, 243, 0.7)' : _ref$maskColor;

  var _useStore = useStore(selector, shallow),
      containerWidth = _useStore.width,
      containerHeight = _useStore.height,
      transform = _useStore.transform,
      nodeInternals = _useStore.nodeInternals;

  var _transform = _slicedToArray(transform, 3),
      tX = _transform[0],
      tY = _transform[1],
      tScale = _transform[2];

  var mapClasses = cc(['react-flow__minimap', className]);
  var elementWidth = (style === null || style === void 0 ? void 0 : style.width) || defaultWidth;
  var elementHeight = (style === null || style === void 0 ? void 0 : style.height) || defaultHeight;
  var nodeColorFunc = nodeColor instanceof Function ? nodeColor : function () {
    return nodeColor;
  };
  var nodeStrokeColorFunc = nodeStrokeColor instanceof Function ? nodeStrokeColor : function () {
    return nodeStrokeColor;
  };
  var nodeClassNameFunc = nodeClassName instanceof Function ? nodeClassName : function () {
    return nodeClassName;
  };
  var hasNodes = nodeInternals && nodeInternals.size > 0; // @TODO: work with nodeInternals instead of converting it to an array

  var nodes = Array.from(nodeInternals).map(function (_ref2) {
    var _ref3 = _slicedToArray(_ref2, 2);
        _ref3[0];
        var node = _ref3[1];

    return node;
  });
  var bb = getRectOfNodes(nodes);
  var viewBB = {
    x: -tX / tScale,
    y: -tY / tScale,
    width: containerWidth / tScale,
    height: containerHeight / tScale
  };
  var boundingRect = hasNodes ? getBoundsofRects(bb, viewBB) : viewBB;
  var scaledWidth = boundingRect.width / elementWidth;
  var scaledHeight = boundingRect.height / elementHeight;
  var viewScale = Math.max(scaledWidth, scaledHeight);
  var viewWidth = viewScale * elementWidth;
  var viewHeight = viewScale * elementHeight;
  var offset = 5 * viewScale;
  var x = boundingRect.x - (viewWidth - boundingRect.width) / 2 - offset;
  var y = boundingRect.y - (viewHeight - boundingRect.height) / 2 - offset;
  var width = viewWidth + offset * 2;
  var height = viewHeight + offset * 2;
  var shapeRendering = typeof window === 'undefined' || !!window.chrome ? 'crispEdges' : 'geometricPrecision';
  return /*#__PURE__*/React__default.createElement("svg", {
    width: elementWidth,
    height: elementHeight,
    viewBox: "".concat(x, " ").concat(y, " ").concat(width, " ").concat(height),
    style: style,
    className: mapClasses
  }, Array.from(nodeInternals).filter(function (_ref4) {
    var _ref5 = _slicedToArray(_ref4, 2);
        _ref5[0];
        var node = _ref5[1];

    return !node.hidden && node.width && node.height;
  }).map(function (_ref6) {
    var _nodeInternals$get;

    var _ref7 = _slicedToArray(_ref6, 2);
        _ref7[0];
        var node = _ref7[1];

    var positionAbsolute = (_nodeInternals$get = nodeInternals.get(node.id)) === null || _nodeInternals$get === void 0 ? void 0 : _nodeInternals$get.positionAbsolute;
    return /*#__PURE__*/React__default.createElement(MiniMapNode$1, {
      key: node.id,
      x: (positionAbsolute === null || positionAbsolute === void 0 ? void 0 : positionAbsolute.x) || 0,
      y: (positionAbsolute === null || positionAbsolute === void 0 ? void 0 : positionAbsolute.y) || 0,
      width: node.width,
      height: node.height,
      style: node.style,
      className: nodeClassNameFunc(node),
      color: nodeColorFunc(node),
      borderRadius: nodeBorderRadius,
      strokeColor: nodeStrokeColorFunc(node),
      strokeWidth: nodeStrokeWidth,
      shapeRendering: shapeRendering
    });
  }), /*#__PURE__*/React__default.createElement("path", {
    className: "react-flow__minimap-mask",
    d: "M".concat(x - offset, ",").concat(y - offset, "h").concat(width + offset * 2, "v").concat(height + offset * 2, "h").concat(-width - offset * 2, "z\n        M").concat(viewBB.x, ",").concat(viewBB.y, "h").concat(viewBB.width, "v").concat(viewBB.height, "h").concat(-viewBB.width, "z"),
    fill: maskColor,
    fillRule: "evenodd"
  }));
};

MiniMap.displayName = 'MiniMap';
var index = /*#__PURE__*/memo(MiniMap);

export { index as default };
//# sourceMappingURL=index2.js.map
