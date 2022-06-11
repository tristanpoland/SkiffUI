import { u as useStoreApi, _ as _slicedToArray, b as useStore, a as _defineProperty } from './index-fdcea71e.js';
import { a as _objectWithoutProperties, u as useReactFlow } from './useReactFlow-0b93bbea.js';
import * as React from 'react';
import React__default, { memo, useState, useCallback, useEffect } from 'react';
import cc from 'classcat';
import 'zustand';
import 'zustand/context';
import 'd3-zoom';
import 'zustand/shallow';

var _path$4;

function _extends$4() { _extends$4 = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends$4.apply(this, arguments); }

var SvgPlus = function SvgPlus(props) {
  return /*#__PURE__*/React.createElement("svg", _extends$4({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 32 32"
  }, props), _path$4 || (_path$4 = /*#__PURE__*/React.createElement("path", {
    d: "M32 18.133H18.133V32h-4.266V18.133H0v-4.266h13.867V0h4.266v13.867H32z"
  })));
};

var _path$3;

function _extends$3() { _extends$3 = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends$3.apply(this, arguments); }

var SvgMinus = function SvgMinus(props) {
  return /*#__PURE__*/React.createElement("svg", _extends$3({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 32 5"
  }, props), _path$3 || (_path$3 = /*#__PURE__*/React.createElement("path", {
    d: "M0 0h32v4.2H0z"
  })));
};

var _path$2;

function _extends$2() { _extends$2 = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends$2.apply(this, arguments); }

var SvgFitview = function SvgFitview(props) {
  return /*#__PURE__*/React.createElement("svg", _extends$2({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 32 30"
  }, props), _path$2 || (_path$2 = /*#__PURE__*/React.createElement("path", {
    d: "M3.692 4.63c0-.53.4-.938.939-.938h5.215V0H4.708C2.13 0 0 2.054 0 4.63v5.216h3.692V4.631zM27.354 0h-5.2v3.692h5.17c.53 0 .984.4.984.939v5.215H32V4.631A4.624 4.624 0 0 0 27.354 0zm.954 24.83c0 .532-.4.94-.939.94h-5.215v3.768h5.215c2.577 0 4.631-2.13 4.631-4.707v-5.139h-3.692v5.139zm-23.677.94a.919.919 0 0 1-.939-.94v-5.138H0v5.139c0 2.577 2.13 4.707 4.708 4.707h5.138V25.77H4.631z"
  })));
};

var _path$1;

function _extends$1() { _extends$1 = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends$1.apply(this, arguments); }

var SvgLock = function SvgLock(props) {
  return /*#__PURE__*/React.createElement("svg", _extends$1({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 25 32"
  }, props), _path$1 || (_path$1 = /*#__PURE__*/React.createElement("path", {
    d: "M21.333 10.667H19.81V7.619C19.81 3.429 16.38 0 12.19 0 8 0 4.571 3.429 4.571 7.619v3.048H3.048A3.056 3.056 0 0 0 0 13.714v15.238A3.056 3.056 0 0 0 3.048 32h18.285a3.056 3.056 0 0 0 3.048-3.048V13.714a3.056 3.056 0 0 0-3.048-3.047zM12.19 24.533a3.056 3.056 0 0 1-3.047-3.047 3.056 3.056 0 0 1 3.047-3.048 3.056 3.056 0 0 1 3.048 3.048 3.056 3.056 0 0 1-3.048 3.047zm4.724-13.866H7.467V7.619c0-2.59 2.133-4.724 4.723-4.724 2.591 0 4.724 2.133 4.724 4.724v3.048z"
  })));
};

var _path;

function _extends() { _extends = Object.assign || function (target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i]; for (var key in source) { if (Object.prototype.hasOwnProperty.call(source, key)) { target[key] = source[key]; } } } return target; }; return _extends.apply(this, arguments); }

var SvgUnlock = function SvgUnlock(props) {
  return /*#__PURE__*/React.createElement("svg", _extends({
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 25 32"
  }, props), _path || (_path = /*#__PURE__*/React.createElement("path", {
    d: "M21.333 10.667H19.81V7.619C19.81 3.429 16.38 0 12.19 0c-4.114 1.828-1.37 2.133.305 2.438 1.676.305 4.42 2.59 4.42 5.181v3.048H3.047A3.056 3.056 0 0 0 0 13.714v15.238A3.056 3.056 0 0 0 3.048 32h18.285a3.056 3.056 0 0 0 3.048-3.048V13.714a3.056 3.056 0 0 0-3.048-3.047zM12.19 24.533a3.056 3.056 0 0 1-3.047-3.047 3.056 3.056 0 0 1 3.047-3.048 3.056 3.056 0 0 1 3.048 3.048 3.056 3.056 0 0 1-3.048 3.047z"
  })));
};

var _excluded = ["children", "className"];

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); enumerableOnly && (symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; })), keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = null != arguments[i] ? arguments[i] : {}; i % 2 ? ownKeys(Object(source), !0).forEach(function (key) { _defineProperty(target, key, source[key]); }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)) : ownKeys(Object(source)).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } return target; }
var ControlButton = function ControlButton(_ref) {
  var children = _ref.children,
      className = _ref.className,
      rest = _objectWithoutProperties(_ref, _excluded);

  return /*#__PURE__*/React__default.createElement("button", _objectSpread({
    type: "button",
    className: cc(['react-flow__controls-button', className])
  }, rest), children);
};

var isInteractiveSelector = function isInteractiveSelector(s) {
  return s.nodesDraggable && s.nodesConnectable && s.elementsSelectable;
};

var Controls = function Controls(_ref2) {
  var style = _ref2.style,
      _ref2$showZoom = _ref2.showZoom,
      showZoom = _ref2$showZoom === void 0 ? true : _ref2$showZoom,
      _ref2$showFitView = _ref2.showFitView,
      showFitView = _ref2$showFitView === void 0 ? true : _ref2$showFitView,
      _ref2$showInteractive = _ref2.showInteractive,
      showInteractive = _ref2$showInteractive === void 0 ? true : _ref2$showInteractive,
      fitViewOptions = _ref2.fitViewOptions,
      onZoomIn = _ref2.onZoomIn,
      onZoomOut = _ref2.onZoomOut,
      onFitView = _ref2.onFitView,
      onInteractiveChange = _ref2.onInteractiveChange,
      className = _ref2.className,
      children = _ref2.children;
  var store = useStoreApi();

  var _useState = useState(false),
      _useState2 = _slicedToArray(_useState, 2),
      isVisible = _useState2[0],
      setIsVisible = _useState2[1];

  var isInteractive = useStore(isInteractiveSelector);

  var _useReactFlow = useReactFlow(),
      zoomIn = _useReactFlow.zoomIn,
      zoomOut = _useReactFlow.zoomOut,
      fitView = _useReactFlow.fitView;

  var mapClasses = cc(['react-flow__controls', className]);
  var onZoomInHandler = useCallback(function () {
    zoomIn === null || zoomIn === void 0 ? void 0 : zoomIn();
    onZoomIn === null || onZoomIn === void 0 ? void 0 : onZoomIn();
  }, [zoomIn, onZoomIn]);
  var onZoomOutHandler = useCallback(function () {
    zoomOut === null || zoomOut === void 0 ? void 0 : zoomOut();
    onZoomOut === null || onZoomOut === void 0 ? void 0 : onZoomOut();
  }, [zoomOut, onZoomOut]);
  var onFitViewHandler = useCallback(function () {
    fitView === null || fitView === void 0 ? void 0 : fitView(fitViewOptions);
    onFitView === null || onFitView === void 0 ? void 0 : onFitView();
  }, [fitView, fitViewOptions, onFitView]);
  var onInteractiveChangeHandler = useCallback(function () {
    store.setState({
      nodesDraggable: !isInteractive,
      nodesConnectable: !isInteractive,
      elementsSelectable: !isInteractive
    });
    onInteractiveChange === null || onInteractiveChange === void 0 ? void 0 : onInteractiveChange(!isInteractive);
  }, [isInteractive, onInteractiveChange]);
  useEffect(function () {
    setIsVisible(true);
  }, []);

  if (!isVisible) {
    return null;
  }

  return /*#__PURE__*/React__default.createElement("div", {
    className: mapClasses,
    style: style
  }, showZoom && /*#__PURE__*/React__default.createElement(React__default.Fragment, null, /*#__PURE__*/React__default.createElement(ControlButton, {
    onClick: onZoomInHandler,
    className: "react-flow__controls-zoomin",
    title: "zoom in",
    "aria-label": "zoom in"
  }, /*#__PURE__*/React__default.createElement(SvgPlus, null)), /*#__PURE__*/React__default.createElement(ControlButton, {
    onClick: onZoomOutHandler,
    className: "react-flow__controls-zoomout",
    title: "zoom out",
    "aria-label": "zoom out"
  }, /*#__PURE__*/React__default.createElement(SvgMinus, null))), showFitView && /*#__PURE__*/React__default.createElement(ControlButton, {
    className: "react-flow__controls-fitview",
    onClick: onFitViewHandler,
    title: "fit view",
    "aria-label": "fit view"
  }, /*#__PURE__*/React__default.createElement(SvgFitview, null)), showInteractive && /*#__PURE__*/React__default.createElement(ControlButton, {
    className: "react-flow__controls-interactive",
    onClick: onInteractiveChangeHandler,
    title: "toggle interactivity",
    "aria-label": "toggle interactivity"
  }, isInteractive ? /*#__PURE__*/React__default.createElement(SvgUnlock, null) : /*#__PURE__*/React__default.createElement(SvgLock, null)), children);
};

Controls.displayName = 'Controls';
var index = /*#__PURE__*/memo(Controls);

export { ControlButton, index as default };
//# sourceMappingURL=index3.js.map
