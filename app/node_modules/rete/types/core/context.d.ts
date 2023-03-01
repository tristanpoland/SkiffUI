import { Component } from '../engine/component';
import { Emitter } from './emitter';
import { EventsTypes as DefaultEvents, Events } from './events';
import { Plugin, PluginParams } from './plugin';
export declare class Context<EventsTypes> extends Emitter<EventsTypes & DefaultEvents> {
    id: string;
    plugins: Map<string, unknown>;
    components: Map<string, Component>;
    constructor(id: string, events: Events);
    use<T extends Plugin, O extends PluginParams<T>>(plugin: T, options?: O): void;
    register(component: Component): void;
    destroy(): void;
}
