import { Control } from '../control';
import { Emitter } from '../core/emitter';
import { EventsTypes } from '../events';
export declare class ControlView extends Emitter<EventsTypes> {
    constructor(el: HTMLElement, control: Control, emitter: Emitter<EventsTypes>);
}
