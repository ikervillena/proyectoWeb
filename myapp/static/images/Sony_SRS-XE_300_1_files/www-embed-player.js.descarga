(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
'use strict';var k;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function da(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var fa=da(this);function n(a,b){if(b)a:{var c=fa;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ba(c,a,{configurable:!0,writable:!0,value:b})}}
n("Symbol",function(a){function b(f){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c(d+(f||"")+"_"+e++,f)}
function c(f,g){this.h=f;ba(this,"description",{configurable:!0,writable:!0,value:g})}
if(a)return a;c.prototype.toString=function(){return this.h};
var d="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",e=0;return b});
n("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=fa[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ha(aa(this))}})}return a});
function ha(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function ia(a){return a.raw=a}
function p(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function ja(a){if(!(a instanceof Array)){a=p(a);for(var b,c=[];!(b=a.next()).done;)c.push(b.value);a=c}return a}
function ka(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var la="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)ka(d,e)&&(a[e]=d[e])}return a};
n("Object.assign",function(a){return a||la});
var na="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},pa=function(){function a(){function c(){}
new c;Reflect.construct(c,[],function(){});
return new c instanceof c}
if("undefined"!=typeof Reflect&&Reflect.construct){if(a())return Reflect.construct;var b=Reflect.construct;return function(c,d,e){c=b(c,d);e&&Reflect.setPrototypeOf(c,e.prototype);return c}}return function(c,d,e){void 0===e&&(e=c);
e=na(e.prototype||Object.prototype);return Function.prototype.apply.call(c,e,d)||e}}(),qa;
if("function"==typeof Object.setPrototypeOf)qa=Object.setPrototypeOf;else{var sa;a:{var ta={a:!0},ua={};try{ua.__proto__=ta;sa=ua.a;break a}catch(a){}sa=!1}qa=sa?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var va=qa;
function u(a,b){a.prototype=na(b.prototype);a.prototype.constructor=a;if(va)va(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.Y=b.prototype}
function wa(){this.v=!1;this.l=null;this.i=void 0;this.h=1;this.m=this.o=0;this.s=this.j=null}
function xa(a){if(a.v)throw new TypeError("Generator is already running");a.v=!0}
wa.prototype.M=function(a){this.i=a};
function ya(a,b){a.j={Yb:b,fc:!0};a.h=a.o||a.m}
wa.prototype.return=function(a){this.j={return:a};this.h=this.m};
function v(a,b,c){a.h=c;return{value:b}}
wa.prototype.u=function(a){this.h=a};
function za(a,b,c){a.o=b;void 0!=c&&(a.m=c)}
function Aa(a,b){a.h=b;a.o=0}
function Ba(a){a.o=0;var b=a.j.Yb;a.j=null;return b}
function Ca(a){a.s=[a.j];a.o=0;a.m=0}
function Da(a){var b=a.s.splice(0)[0];(b=a.j=a.j||b)?b.fc?a.h=a.o||a.m:void 0!=b.u&&a.m<b.u?(a.h=b.u,a.j=null):a.h=a.m:a.h=0}
function Ea(a){this.h=new wa;this.i=a}
function Fa(a,b){xa(a.h);var c=a.h.l;if(c)return Ga(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.h.return);
a.h.return(b);return Ha(a)}
function Ga(a,b,c,d){try{var e=b.call(a.h.l,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.h.v=!1,e;var f=e.value}catch(g){return a.h.l=null,ya(a.h,g),Ha(a)}a.h.l=null;d.call(a.h,f);return Ha(a)}
function Ha(a){for(;a.h.h;)try{var b=a.i(a.h);if(b)return a.h.v=!1,{value:b.value,done:!1}}catch(c){a.h.i=void 0,ya(a.h,c)}a.h.v=!1;if(a.h.j){b=a.h.j;a.h.j=null;if(b.fc)throw b.Yb;return{value:b.return,done:!0}}return{value:void 0,done:!0}}
function Ia(a){this.next=function(b){xa(a.h);a.h.l?b=Ga(a,a.h.l.next,b,a.h.M):(a.h.M(b),b=Ha(a));return b};
this.throw=function(b){xa(a.h);a.h.l?b=Ga(a,a.h.l["throw"],b,a.h.M):(ya(a.h,b),b=Ha(a));return b};
this.return=function(b){return Fa(a,b)};
this[Symbol.iterator]=function(){return this}}
function Ja(a){function b(d){return a.next(d)}
function c(d){return a.throw(d)}
return new Promise(function(d,e){function f(g){g.done?d(g.value):Promise.resolve(g.value).then(b,c).then(f,e)}
f(a.next())})}
function x(a){return Ja(new Ia(new Ea(a)))}
function Ka(){for(var a=Number(this),b=[],c=a;c<arguments.length;c++)b[c-a]=arguments[c];return b}
n("Reflect",function(a){return a?a:{}});
n("Reflect.construct",function(){return pa});
n("Reflect.setPrototypeOf",function(a){return a?a:va?function(b,c){try{return va(b,c),!0}catch(d){return!1}}:null});
n("Promise",function(a){function b(g){this.h=0;this.j=void 0;this.i=[];this.v=!1;var h=this.l();try{g(h.resolve,h.reject)}catch(l){h.reject(l)}}
function c(){this.h=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.i=function(g){if(null==this.h){this.h=[];var h=this;this.j(function(){h.m()})}this.h.push(g)};
var e=fa.setTimeout;c.prototype.j=function(g){e(g,0)};
c.prototype.m=function(){for(;this.h&&this.h.length;){var g=this.h;this.h=[];for(var h=0;h<g.length;++h){var l=g[h];g[h]=null;try{l()}catch(m){this.l(m)}}}this.h=null};
c.prototype.l=function(g){this.j(function(){throw g;})};
b.prototype.l=function(){function g(m){return function(q){l||(l=!0,m.call(h,q))}}
var h=this,l=!1;return{resolve:g(this.K),reject:g(this.m)}};
b.prototype.K=function(g){if(g===this)this.m(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.P(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.I(g):this.o(g)}};
b.prototype.I=function(g){var h=void 0;try{h=g.then}catch(l){this.m(l);return}"function"==typeof h?this.T(h,g):this.o(g)};
b.prototype.m=function(g){this.M(2,g)};
b.prototype.o=function(g){this.M(1,g)};
b.prototype.M=function(g,h){if(0!=this.h)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.h);this.h=g;this.j=h;2===this.h&&this.O();this.s()};
b.prototype.O=function(){var g=this;e(function(){if(g.F()){var h=fa.console;"undefined"!==typeof h&&h.error(g.j)}},1)};
b.prototype.F=function(){if(this.v)return!1;var g=fa.CustomEvent,h=fa.Event,l=fa.dispatchEvent;if("undefined"===typeof l)return!0;"function"===typeof g?g=new g("unhandledrejection",{cancelable:!0}):"function"===typeof h?g=new h("unhandledrejection",{cancelable:!0}):(g=fa.document.createEvent("CustomEvent"),g.initCustomEvent("unhandledrejection",!1,!0,g));g.promise=this;g.reason=this.j;return l(g)};
b.prototype.s=function(){if(null!=this.i){for(var g=0;g<this.i.length;++g)f.i(this.i[g]);this.i=null}};
var f=new c;b.prototype.P=function(g){var h=this.l();g.eb(h.resolve,h.reject)};
b.prototype.T=function(g,h){var l=this.l();try{g.call(h,l.resolve,l.reject)}catch(m){l.reject(m)}};
b.prototype.then=function(g,h){function l(w,t){return"function"==typeof w?function(A){try{m(w(A))}catch(E){q(E)}}:t}
var m,q,r=new b(function(w,t){m=w;q=t});
this.eb(l(g,m),l(h,q));return r};
b.prototype.catch=function(g){return this.then(void 0,g)};
b.prototype.eb=function(g,h){function l(){switch(m.h){case 1:g(m.j);break;case 2:h(m.j);break;default:throw Error("Unexpected state: "+m.h);}}
var m=this;null==this.i?f.i(l):this.i.push(l);this.v=!0};
b.resolve=d;b.reject=function(g){return new b(function(h,l){l(g)})};
b.race=function(g){return new b(function(h,l){for(var m=p(g),q=m.next();!q.done;q=m.next())d(q.value).eb(h,l)})};
b.all=function(g){var h=p(g),l=h.next();return l.done?d([]):new b(function(m,q){function r(A){return function(E){w[A]=E;t--;0==t&&m(w)}}
var w=[],t=0;do w.push(void 0),t++,d(l.value).eb(r(w.length-1),q),l=h.next();while(!l.done)})};
return b});
n("WeakMap",function(a){function b(l){this.h=(h+=Math.random()+1).toString();if(l){l=p(l);for(var m;!(m=l.next()).done;)m=m.value,this.set(m[0],m[1])}}
function c(){}
function d(l){var m=typeof l;return"object"===m&&null!==l||"function"===m}
function e(l){if(!ka(l,g)){var m=new c;ba(l,g,{value:m})}}
function f(l){var m=Object[l];m&&(Object[l]=function(q){if(q instanceof c)return q;Object.isExtensible(q)&&e(q);return m(q)})}
if(function(){if(!a||!Object.seal)return!1;try{var l=Object.seal({}),m=Object.seal({}),q=new a([[l,2],[m,3]]);if(2!=q.get(l)||3!=q.get(m))return!1;q.delete(l);q.set(m,4);return!q.has(l)&&4==q.get(m)}catch(r){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(l,m){if(!d(l))throw Error("Invalid WeakMap key");e(l);if(!ka(l,g))throw Error("WeakMap key fail: "+l);l[g][this.h]=m;return this};
b.prototype.get=function(l){return d(l)&&ka(l,g)?l[g][this.h]:void 0};
b.prototype.has=function(l){return d(l)&&ka(l,g)&&ka(l[g],this.h)};
b.prototype.delete=function(l){return d(l)&&ka(l,g)&&ka(l[g],this.h)?delete l[g][this.h]:!1};
return b});
n("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,l){var m=h.h;return ha(function(){if(m){for(;m.head!=h.h;)m=m.previous;for(;m.next!=m.head;)return m=m.next,{done:!1,value:l(m)};m=null}return{done:!0,value:void 0}})}
function d(h,l){var m=l&&typeof l;"object"==m||"function"==m?f.has(l)?m=f.get(l):(m=""+ ++g,f.set(l,m)):m="p_"+l;var q=h.data_[m];if(q&&ka(h.data_,m))for(h=0;h<q.length;h++){var r=q[h];if(l!==l&&r.key!==r.key||l===r.key)return{id:m,list:q,index:h,entry:r}}return{id:m,list:q,index:-1,entry:void 0}}
function e(h){this.data_={};this.h=b();this.size=0;if(h){h=p(h);for(var l;!(l=h.next()).done;)l=l.value,this.set(l[0],l[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),l=new a(p([[h,"s"]]));if("s"!=l.get(h)||1!=l.size||l.get({x:4})||l.set({x:4},"t")!=l||2!=l.size)return!1;var m=l.entries(),q=m.next();if(q.done||q.value[0]!=h||"s"!=q.value[1])return!1;q=m.next();return q.done||4!=q.value[0].x||"t"!=q.value[1]||!m.next().done?!1:!0}catch(r){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,l){h=0===h?0:h;var m=d(this,h);m.list||(m.list=this.data_[m.id]=[]);m.entry?m.entry.value=l:(m.entry={next:this.h,previous:this.h.previous,head:this.h,key:h,value:l},m.list.push(m.entry),this.h.previous.next=m.entry,this.h.previous=m.entry,this.size++);return this};
e.prototype.delete=function(h){h=d(this,h);return h.entry&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.data_[h.id],h.entry.previous.next=h.entry.next,h.entry.next.previous=h.entry.previous,h.entry.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.data_={};this.h=this.h.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).entry};
e.prototype.get=function(h){return(h=d(this,h).entry)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,l){for(var m=this.entries(),q;!(q=m.next()).done;)q=q.value,h.call(l,q[1],q[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
function La(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
n("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=La(this,b,"endsWith");b+="";void 0===c&&(c=d.length);c=Math.max(0,Math.min(c|0,d.length));for(var e=b.length;0<e&&0<c;)if(d[--c]!=b[--e])return!1;return 0>=e}});
n("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});
n("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=La(this,b,"startsWith");b+="";var e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});
n("Number.isFinite",function(a){return a?a:function(b){return"number"!==typeof b?!1:!isNaN(b)&&Infinity!==b&&-Infinity!==b}});
n("Number.isInteger",function(a){return a?a:function(b){return Number.isFinite(b)?b===Math.floor(b):!1}});
n("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
n("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});
function Ma(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};
e[Symbol.iterator]=function(){return e};
return e}
n("Array.prototype.entries",function(a){return a?a:function(){return Ma(this,function(b,c){return[b,c]})}});
n("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};
var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
n("Array.prototype.keys",function(a){return a?a:function(){return Ma(this,function(b){return b})}});
n("Array.prototype.values",function(a){return a?a:function(){return Ma(this,function(b,c){return c})}});
n("Array.prototype.fill",function(a){return a?a:function(b,c,d){var e=this.length||0;0>c&&(c=Math.max(0,e+c));if(null==d||d>e)d=e;d=Number(d);0>d&&(d=Math.max(0,e+d));for(c=Number(c||0);c<d;c++)this[c]=b;return this}});
function Na(a){return a?a:Array.prototype.fill}
n("Int8Array.prototype.fill",Na);n("Uint8Array.prototype.fill",Na);n("Uint8ClampedArray.prototype.fill",Na);n("Int16Array.prototype.fill",Na);n("Uint16Array.prototype.fill",Na);n("Int32Array.prototype.fill",Na);n("Uint32Array.prototype.fill",Na);n("Float32Array.prototype.fill",Na);n("Float64Array.prototype.fill",Na);n("Object.setPrototypeOf",function(a){return a||va});
n("Set",function(a){function b(c){this.h=new Map;if(c){c=p(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.h.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(p([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.h.set(c,c);this.size=this.h.size;return this};
b.prototype.delete=function(c){c=this.h.delete(c);this.size=this.h.size;return c};
b.prototype.clear=function(){this.h.clear();this.size=0};
b.prototype.has=function(c){return this.h.has(c)};
b.prototype.entries=function(){return this.h.entries()};
b.prototype.values=function(){return this.h.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.h.forEach(function(f){return c.call(d,f,f,e)})};
return b});
n("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)ka(b,d)&&c.push([d,b[d]]);return c}});
n("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
n("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});
n("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==La(this,b,"includes").indexOf(b,c||0)}});
n("globalThis",function(a){return a||fa});
n("Object.values",function(a){return a?a:function(b){var c=[],d;for(d in b)ka(b,d)&&c.push(b[d]);return c}});
var Oa=Oa||{},y=this||self;function z(a,b,c){a=a.split(".");c=c||y;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function B(a,b){a=a.split(".");b=b||y;for(var c=0;c<a.length;c++)if(b=b[a[c]],null==b)return null;return b}
function Pa(a){a.zb=void 0;a.getInstance=function(){return a.zb?a.zb:a.zb=new a}}
function Qa(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Ra(a){var b=Qa(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Sa(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Ta(a){return Object.prototype.hasOwnProperty.call(a,Ua)&&a[Ua]||(a[Ua]=++Va)}
var Ua="closure_uid_"+(1E9*Math.random()>>>0),Va=0;function Xa(a,b,c){return a.call.apply(a.bind,arguments)}
function Ya(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function Za(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?Za=Xa:Za=Ya;return Za.apply(null,arguments)}
function $a(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function ab(a,b){function c(){}
c.prototype=b.prototype;a.Y=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.wr=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
function bb(a){return a}
;function cb(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,cb);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)}
ab(cb,Error);cb.prototype.name="CustomError";function db(a){a=a.url;var b=/[?&]dsh=1(&|$)/.test(a);this.j=!b&&/[?&]ae=1(&|$)/.test(a);this.l=!b&&/[?&]ae=2(&|$)/.test(a);if((this.h=/[?&]adurl=([^&]*)/.exec(a))&&this.h[1]){try{var c=decodeURIComponent(this.h[1])}catch(d){c=null}this.i=c}}
;function eb(){}
function fb(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;var gb=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},hb=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},ib=Array.prototype.filter?function(a,b){return Array.prototype.filter.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=[],e=0,f="string"===typeof a?a.split(""):a,g=0;g<c;g++)if(g in f){var h=f[g];
b.call(void 0,h,g,a)&&(d[e++]=h)}return d},jb=Array.prototype.map?function(a,b){return Array.prototype.map.call(a,b,void 0)}:function(a,b){for(var c=a.length,d=Array(c),e="string"===typeof a?a.split(""):a,f=0;f<c;f++)f in e&&(d[f]=b.call(void 0,e[f],f,a));
return d},kb=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
hb(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function lb(a,b){a:{for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return 0>b?null:"string"===typeof a?a.charAt(b):a[b]}
function mb(a,b){b=gb(a,b);var c;(c=0<=b)&&Array.prototype.splice.call(a,b,1);return c}
function nb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Ra(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function ob(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function pb(a){var b=qb,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function sb(a){for(var b in a)return!1;return!0}
function tb(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function ub(a){return null!==a&&"privembed"in a?a.privembed:!1}
function vb(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function wb(a){var b={},c;for(c in a)b[c]=a[c];return b}
function xb(a){if(!a||"object"!==typeof a)return a;if("function"===typeof a.clone)return a.clone();if("undefined"!==typeof Map&&a instanceof Map)return new Map(a);if("undefined"!==typeof Set&&a instanceof Set)return new Set(a);if(a instanceof Date)return new Date(a.getTime());var b=Array.isArray(a)?[]:"function"!==typeof ArrayBuffer||"function"!==typeof ArrayBuffer.isView||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length),c;for(c in a)b[c]=xb(a[c]);return b}
var yb="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function zb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<yb.length;f++)c=yb[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var Ab;function Bb(){if(void 0===Ab){var a=null,b=y.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:bb,createScript:bb,createScriptURL:bb})}catch(c){y.console&&y.console.error(c.message)}Ab=a}else Ab=a}return Ab}
;function Cb(a,b){this.j=a===Db&&b||""}
Cb.prototype.i=!0;Cb.prototype.h=function(){return this.j};
function Eb(a){return new Cb(Db,a)}
var Db={};Eb("");var Fb={};function Gb(a){this.j=Fb===Fb?a:"";this.i=!0}
Gb.prototype.toString=function(){return this.j.toString()};
Gb.prototype.h=function(){return this.j.toString()};function Hb(a,b){this.j=b===Ib?a:""}
Hb.prototype.toString=function(){return this.j+""};
Hb.prototype.i=!0;Hb.prototype.h=function(){return this.j.toString()};
function Lb(a){if(a instanceof Hb&&a.constructor===Hb)return a.j;Qa(a);return"type_error:TrustedResourceUrl"}
var Ib={};function Mb(a){var b=Bb();a=b?b.createScriptURL(a):a;return new Hb(a,Ib)}
;var Nb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
function Ob(a,b){return a<b?-1:a>b?1:0}
;function Pb(a,b){this.j=b===Qb?a:""}
Pb.prototype.toString=function(){return this.j.toString()};
Pb.prototype.i=!0;Pb.prototype.h=function(){return this.j.toString()};
function Rb(a){if(a instanceof Pb&&a.constructor===Pb)return a.j;Qa(a);return"type_error:SafeUrl"}
var Sb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i,Qb={},Tb=new Pb("about:invalid#zClosurez",Qb);function Ub(){var a=y.navigator;return a&&(a=a.userAgent)?a:""}
function C(a){return-1!=Ub().indexOf(a)}
;function Vb(){return C("Trident")||C("MSIE")}
function Wb(){return C("Firefox")||C("FxiOS")}
function Xb(){return C("Safari")&&!(Yb()||C("Coast")||C("Opera")||C("Edge")||C("Edg/")||C("OPR")||Wb()||C("Silk")||C("Android"))}
function Yb(){return(C("Chrome")||C("CriOS"))&&!C("Edge")||C("Silk")}
function Zb(){return C("Android")&&!(Yb()||Wb()||C("Opera")||C("Silk"))}
function bc(a){var b={};a.forEach(function(c){b[c[0]]=c[1]});
return function(c){return b[c.find(function(d){return d in b})]||""}}
function cc(a){var b=Ub();if("Internet Explorer"===a){if(Vb())if((a=/rv: *([\d\.]*)/.exec(b))&&a[1])b=a[1];else{a="";var c=/MSIE +([\d\.]+)/.exec(b);if(c&&c[1])if(b=/Trident\/(\d.\d)/.exec(b),"7.0"==c[1])if(b&&b[1])switch(b[1]){case "4.0":a="8.0";break;case "5.0":a="9.0";break;case "6.0":a="10.0";break;case "7.0":a="11.0"}else a="7.0";else a=c[1];b=a}else b="";return b}var d=RegExp("([A-Z][\\w ]+)/([^\\s]+)\\s*(?:\\((.*?)\\))?","g");c=[];for(var e;e=d.exec(b);)c.push([e[1],e[2],e[3]||void 0]);b=bc(c);
switch(a){case "Opera":if(C("Opera"))return b(["Version","Opera"]);if(C("OPR"))return b(["OPR"]);break;case "Microsoft Edge":if(C("Edge"))return b(["Edge"]);if(C("Edg/"))return b(["Edg"]);break;case "Chromium":if(Yb())return b(["Chrome","CriOS","HeadlessChrome"])}return"Firefox"===a&&Wb()||"Safari"===a&&Xb()||"Android Browser"===a&&Zb()||"Silk"===a&&C("Silk")?(b=c[2])&&b[1]||"":""}
function dc(a){a=cc(a);if(""===a)return NaN;a=a.split(".");return 0===a.length?NaN:Number(a[0])}
;var ec={};function fc(a){this.j=ec===ec?a:"";this.i=!0}
fc.prototype.h=function(){return this.j.toString()};
fc.prototype.toString=function(){return this.j.toString()};function gc(a,b){b instanceof Pb||b instanceof Pb||(b="object"==typeof b&&b.i?b.h():String(b),Sb.test(b)||(b="about:invalid#zClosurez"),b=new Pb(b,Qb));a.href=Rb(b)}
function hc(a,b){a.rel="stylesheet";a.href=Lb(b).toString();(b=ic('style[nonce],link[rel="stylesheet"][nonce]',a.ownerDocument&&a.ownerDocument.defaultView))&&a.setAttribute("nonce",b)}
function jc(){return ic("script[nonce]")}
var kc=/^[\w+/_-]+[=]{0,2}$/;function ic(a,b){b=(b||y).document;return b.querySelector?(a=b.querySelector(a))&&(a=a.nonce||a.getAttribute("nonce"))&&kc.test(a)?a:"":""}
;function lc(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var mc=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function nc(a){return a?decodeURI(a):a}
function oc(a,b){return b.match(mc)[a]||null}
function pc(a){return nc(oc(3,a))}
function qc(a){var b=a.match(mc);a=b[5];var c=b[6];b=b[7];var d="";a&&(d+=a);c&&(d+="?"+c);b&&(d+="#"+b);return d}
function rc(a,b){if(!b)return a;var c=a.indexOf("#");0>c&&(c=a.length);var d=a.indexOf("?");if(0>d||d>c){d=c;var e=""}else e=a.substring(d+1,c);a=[a.slice(0,d),e,a.slice(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;return a[0]+(a[1]?"?"+a[1]:"")+a[2]}
function sc(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)sc(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function tc(a,b){var c=[];for(b=b||0;b<a.length;b+=2)sc(a[b],a[b+1],c);return c.join("&")}
function uc(a){var b=[],c;for(c in a)sc(c,a[c],b);return b.join("&")}
function vc(a,b){var c=2==arguments.length?tc(arguments[1],0):tc(arguments,1);return rc(a,c)}
function wc(a,b){b=uc(b);return rc(a,b)}
function xc(a,b,c){c=null!=c?"="+encodeURIComponent(String(c)):"";return rc(a,b+c)}
function yc(a,b,c,d){for(var e=c.length;0<=(b=a.indexOf(c,b))&&b<d;){var f=a.charCodeAt(b-1);if(38==f||63==f)if(f=a.charCodeAt(b+e),!f||61==f||38==f||35==f)return b;b+=e+1}return-1}
var Cc=/#|$/,Dc=/[?&]($|#)/;function Ec(a,b){for(var c=a.search(Cc),d=0,e,f=[];0<=(e=yc(a,d,b,c));)f.push(a.substring(d,e)),d=Math.min(a.indexOf("&",e)+1||c,c);f.push(a.slice(d));return f.join("").replace(Dc,"$1")}
;function Fc(a){y.setTimeout(function(){throw a;},0)}
;function Gc(){return C("iPhone")&&!C("iPod")&&!C("iPad")}
function Hc(){var a=Ub(),b="";C("Windows")?(b=/Windows (?:NT|Phone) ([0-9.]+)/,b=(a=b.exec(a))?a[1]:"0.0"):Gc()||C("iPad")||C("iPod")?(b=/(?:iPhone|iPod|iPad|CPU)\s+OS\s+(\S+)/,b=(a=b.exec(a))&&a[1].replace(/_/g,".")):C("Macintosh")?(b=/Mac OS X ([0-9_.]+)/,b=(a=b.exec(a))?a[1].replace(/_/g,"."):"10"):-1!=Ub().toLowerCase().indexOf("kaios")?(b=/(?:KaiOS)\/(\S+)/i,b=(a=b.exec(a))&&a[1]):C("Android")?(b=/Android\s+([^\);]+)(\)|;)/,b=(a=b.exec(a))&&a[1]):C("CrOS")&&(b=/(?:CrOS\s+(?:i686|x86_64)\s+([0-9.]+))/,
b=(a=b.exec(a))&&a[1]);a=0;b=Nb(String(b||"")).split(".");for(var c=Nb("12").split("."),d=Math.max(b.length,c.length),e=0;0==a&&e<d;e++){var f=b[e]||"",g=c[e]||"";do{f=/(\d*)(\D*)(.*)/.exec(f)||["","","",""];g=/(\d*)(\D*)(.*)/.exec(g)||["","","",""];if(0==f[0].length&&0==g[0].length)break;a=Ob(0==f[1].length?0:parseInt(f[1],10),0==g[1].length?0:parseInt(g[1],10))||Ob(0==f[2].length,0==g[2].length)||Ob(f[2],g[2]);f=f[3];g=g[3]}while(0==a)}}
;function Ic(a){Ic[" "](a);return a}
Ic[" "]=function(){};var Jc=C("Opera"),Kc=Vb(),Lc=C("Edge"),Mc=C("Gecko")&&!(-1!=Ub().toLowerCase().indexOf("webkit")&&!C("Edge"))&&!(C("Trident")||C("MSIE"))&&!C("Edge"),Nc=-1!=Ub().toLowerCase().indexOf("webkit")&&!C("Edge"),Oc=C("Android");function Pc(){var a=y.document;return a?a.documentMode:void 0}
var Qc;a:{var Rc="",Sc=function(){var a=Ub();if(Mc)return/rv:([^\);]+)(\)|;)/.exec(a);if(Lc)return/Edge\/([\d\.]+)/.exec(a);if(Kc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(Nc)return/WebKit\/(\S+)/.exec(a);if(Jc)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
Sc&&(Rc=Sc?Sc[1]:"");if(Kc){var Tc=Pc();if(null!=Tc&&Tc>parseFloat(Rc)){Qc=String(Tc);break a}}Qc=Rc}var Uc=Qc,Vc;if(y.document&&Kc){var Wc=Pc();Vc=Wc?Wc:parseInt(Uc,10)||void 0}else Vc=void 0;var Xc=Vc;var Yc=Gc()||C("iPod"),Zc=C("iPad");Zb();Yb();var $c=Xb()&&!(Gc()||C("iPad")||C("iPod"));var ad={},bd=null;function cd(a,b){Ra(a);void 0===b&&(b=0);dd();b=ad[b];for(var c=Array(Math.floor(a.length/3)),d=b[64]||"",e=0,f=0;e<a.length-2;e+=3){var g=a[e],h=a[e+1],l=a[e+2],m=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|l>>6];l=b[l&63];c[f++]=""+m+g+h+l}m=0;l=d;switch(a.length-e){case 2:m=a[e+1],l=b[(m&15)<<2]||d;case 1:a=a[e],c[f]=""+b[a>>2]+b[(a&3)<<4|m>>4]+l+d}return c.join("")}
function ed(a){var b=a.length,c=3*b/4;c%3?c=Math.floor(c):-1!="=.".indexOf(a[b-1])&&(c=-1!="=.".indexOf(a[b-2])?c-2:c-1);var d=new Uint8Array(c),e=0;fd(a,function(f){d[e++]=f});
return e!==c?d.subarray(0,e):d}
function fd(a,b){function c(l){for(;d<a.length;){var m=a.charAt(d++),q=bd[m];if(null!=q)return q;if(!/^[\s\xa0]*$/.test(m))throw Error("Unknown base64 encoding at char: "+m);}return l}
dd();for(var d=0;;){var e=c(-1),f=c(0),g=c(64),h=c(64);if(64===h&&-1===e)break;b(e<<2|f>>4);64!=g&&(b(f<<4&240|g>>2),64!=h&&b(g<<6&192|h))}}
function dd(){if(!bd){bd={};for(var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"],c=0;5>c;c++){var d=a.concat(b[c].split(""));ad[c]=d;for(var e=0;e<d.length;e++){var f=d[e];void 0===bd[f]&&(bd[f]=e)}}}}
;var gd="undefined"!==typeof Uint8Array;function hd(a){return gd&&null!=a&&a instanceof Uint8Array}
var id={};var jd;function kd(a){if(a!==id)throw Error("illegal external caller");}
function ld(a,b){kd(b);this.ba=a;if(null!=a&&0===a.length)throw Error("ByteString should be constructed with non-empty values");}
function md(){return jd||(jd=new ld(null,id))}
ld.prototype.Na=function(){return null==this.ba};
ld.prototype.sizeBytes=function(){kd(id);var a=this.ba;null==a||hd(a)||("string"===typeof a?a=ed(a):(Qa(a),a=null));return(a=null==a?a:this.ba=a)?a.length:0};var nd="function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():void 0;function od(a,b){if(nd)return a[nd]|=b;if(void 0!==a.fa)return a.fa|=b;Object.defineProperties(a,{fa:{value:b,configurable:!0,writable:!0,enumerable:!1}});return b}
function pd(a,b){nd?a[nd]&&(a[nd]&=~b):void 0!==a.fa&&(a.fa&=~b)}
function qd(a){var b;nd?b=a[nd]:b=a.fa;return null==b?0:b}
function rd(a,b){nd?a[nd]=b:void 0!==a.fa?a.fa=b:Object.defineProperties(a,{fa:{value:b,configurable:!0,writable:!0,enumerable:!1}})}
function sd(a){od(a,1);return a}
function xd(a){return!!(qd(a)&2)}
function yd(a){od(a,16);return a}
function zd(a,b){rd(b,(a|0)&-51)}
function Ad(a,b){rd(b,(a|18)&-41)}
;var Bd={};function Cd(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object}
var Dd,Ed,Fd=[];rd(Fd,23);Ed=Object.freeze(Fd);function Gd(a){if(xd(a.C))throw Error("Cannot mutate an immutable Message");}
function Hd(a){var b=a.length;(b=b?a[b-1]:void 0)&&Cd(b)?b.g=1:(b={},a.push((b.g=1,b)))}
;var Id;function Jd(a){return a.displayName||a.name||"unknown type name"}
function Kd(a,b){if(!(a instanceof b))throw Error("Expected instanceof "+Jd(b)+" but got "+(a&&Jd(a.constructor)));return a}
;function Ld(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "object":if(a)if(Array.isArray(a)){if(0!==(qd(a)&128))return a=Array.prototype.slice.call(a),Hd(a),a}else{if(hd(a))return cd(a);if(a instanceof ld){var b=a.ba;return null==b?"":"string"===typeof b?b:a.ba=cd(b)}}}return a}
;function Md(a,b,c,d){if(null!=a){if(Array.isArray(a))a=Nd(a,b,c,void 0!==d);else if(Cd(a)){var e={},f;for(f in a)e[f]=Md(a[f],b,c,d);a=e}else a=b(a,d);return a}}
function Nd(a,b,c,d){var e=qd(a);d=d?!!(e&16):void 0;a=Array.prototype.slice.call(a);for(var f=0;f<a.length;f++)a[f]=Md(a[f],b,c,d);c(e,a);return a}
function Od(a){return a.jb===Bd?a.toJSON():Ld(a)}
function Pd(a){if(!a)return a;if("object"===typeof a){if(hd(a))return new Uint8Array(a);if(a.jb===Bd)return a.clone()}return a}
function Qd(a,b){a&128&&Hd(b)}
;function Rd(a){var b=a.j+a.va;return a.X||(a.X=a.C[b]={})}
function Sd(a,b,c){return-1===b?null:b>=a.j?a.X?a.X[b]:void 0:c&&a.X&&(c=a.X[b],null!=c)?c:a.C[b+a.va]}
function D(a,b,c,d){Gd(a);return Td(a,b,c,d)}
function Td(a,b,c,d){a.l&&(a.l=void 0);if(b>=a.j||d)return Rd(a)[b]=c,a;a.C[b+a.va]=c;(c=a.X)&&b in c&&delete c[b];return a}
function Ud(a,b){a&&xd(b.C)&&xd(a.C);return a}
function Vd(a,b,c,d,e){var f=Sd(a,b,d);Array.isArray(f)||(f=Ed);var g=qd(f);g&1||sd(f);if(e)g&2||od(f,2),c&1||Object.freeze(f);else{e=!(c&2);var h=g&2;c&1||!h?e&&g&16&&!h&&pd(f,16):(f=sd(Array.prototype.slice.call(f)),Td(a,b,f,d))}return f}
function Wd(a,b,c,d){Gd(a);(c=Xd(a,c))&&c!==b&&null!=d&&Td(a,c,void 0,!1);return Td(a,b,d)}
function Xd(a,b){for(var c=0,d=0;d<b.length;d++){var e=b[d];null!=Sd(a,e)&&(0!==c&&Td(a,c,void 0,!1),c=e)}return c}
function Yd(a,b,c,d){var e=d=void 0===d?!1:d,f=Sd(a,c,e);var g=!1;var h=null==f||"object"!==typeof f||(g=Array.isArray(f))||f.jb!==Bd?g?new b(f):void 0:f;h!==f&&null!=h&&(Td(a,c,h,e),od(h.C,qd(a.C)&18));b=Ud(h,a);if(null==b)return b;xd(a.C)||(e=Zd(b),e!==b&&(b=e,Td(a,c,b,d)));return Ud(b,a)}
function $d(a,b,c,d,e,f){a.h||(a.h={});var g=a.h[c],h=Vd(a,c,3,d,f);if(g)f||(Object.isFrozen(g)?e||(g=Array.prototype.slice.call(g),a.h[c]=g):e&&Object.freeze(g));else{g=[];var l=!!(qd(a.C)&16),m=xd(h);!f&&m&&(h=sd(Array.prototype.slice.call(h)),Td(a,c,h,d));d=m;for(var q=0;q<h.length;q++){var r=h[q];var w=b;var t=l,A=!1;A=void 0===A?!1:A;t=void 0===t?!1:t;w=Array.isArray(r)?new w(t?yd(r):r):A?new w:void 0;void 0!==w&&(d=d||xd(r),g.push(w),m&&od(w.C,2))}a.h[c]=g;a=h;b=!d;Object.isFrozen(a)||(c=qd(a)|
33,rd(a,b?c|8:c&-9));(f||e&&m)&&od(g,2);(f||e)&&Object.freeze(g)}return g}
function ae(a,b,c,d){var e=xd(a.C);b=$d(a,b,c,d,e,e);a=Vd(a,c,3,d,e);if(!(e||qd(a)&8)){for(e=0;e<b.length;e++)c=b[e],d=Zd(c),c!==d&&(b[e]=d,a[e]=b[e].C);od(a,8)}return b}
function G(a,b,c,d){Gd(a);null!=d?Kd(d,b):d=void 0;return Td(a,c,d)}
function be(a,b,c,d,e){Gd(a);null!=e?Kd(e,b):e=void 0;Wd(a,c,d,e)}
function ce(a,b,c,d,e){Gd(a);if(null!=d){var f=sd([]);for(var g=!1,h=0;h<d.length;h++)f[h]=Kd(d[h],b).C,g=g||xd(f[h]);a.h||(a.h={});a.h[c]=d;b=f;g?pd(b,8):od(b,8)}else a.h&&(a.h[c]=void 0),f=Ed;return Td(a,c,f,e)}
function de(a,b,c,d){Gd(a);var e=$d(a,c,b,void 0,!1,!1);c=null!=d?Kd(d,c):new c;a=Vd(a,b,2,void 0,!1);e.push(c);a.push(c.C);xd(c.C)&&pd(a,8)}
function ee(a,b){return Sd(a,b)}
function fe(a,b){return null==a?b:a}
;function ge(a,b,c){c=void 0===c?Ad:c;if(null!=a){if(gd&&a instanceof Uint8Array)return a.length?new ld(new Uint8Array(a),id):md();if(Array.isArray(a)){var d=qd(a);if(d&2)return a;if(b&&!(d&32)&&(d&16||0===d))return rd(a,d|2),a;a=Nd(a,ge,c,!0);b=qd(a);b&4&&b&2&&Object.freeze(a);return a}return a.jb===Bd?he(a):a}}
function ie(a,b,c,d,e,f,g){(a=a.h&&a.h[c])?(d=0<a.length?a[0].constructor:void 0,f=qd(a),f&2||(a=jb(a,he),Ad(f,a),Object.freeze(a)),ce(b,d,c,a,e)):D(b,c,ge(d,f,g),e)}
function he(a){if(xd(a.C))return a;a=je(a,!0);od(a.C,2);return a}
function je(a,b){var c=a.C,d=yd([]),e=a.constructor.h;e&&d.push(e);a.X&&(d.length=c.length,d.fill(void 0,d.length,c.length),d[d.length-1]={});0!==(qd(c)&128)&&Hd(d);b=b||xd(a.C)?Ad:zd;e=a.constructor;qd(d);Id=d;d=new e(d);Id=void 0;a.Ma&&(d.Ma=a.Ma.slice());e=!!(qd(c)&16);for(var f=0;f<c.length;f++){var g=c[f];if(f===c.length-1&&Cd(g))for(var h in g){var l=+h;Number.isNaN(l)?Rd(d)[l]=g[l]:ie(a,d,l,g[h],!0,e,b)}else ie(a,d,f-a.va,g,!1,e,b)}return d}
function Zd(a){if(!xd(a.C))return a;var b=je(a,!1);b.l=a;return b}
;function H(a,b,c){null==a&&(a=Id);Id=void 0;var d=this.constructor.i||0,e=0<d,f=this.constructor.h,g=!1;if(null==a){a=f?[f]:[];var h=!0;rd(a,48)}else{if(!Array.isArray(a))throw Error();if(f&&f!==a[0])throw Error();var l=od(a,0),m=l;if(h=0!==(16&m))(g=0!==(32&m))||(m|=32);if(e)if(128&m)d=0;else{if(0<a.length){var q=a[a.length-1];if(Cd(q)&&"g"in q){d=0;m|=128;delete q.g;var r=!0,w;for(w in q){r=!1;break}r&&a.pop()}}}else if(128&m)throw Error();l!==m&&rd(a,m)}this.va=(f?0:-1)-d;this.h=void 0;this.C=
a;a:{f=this.C.length;d=f-1;if(f&&(f=this.C[d],Cd(f))){this.X=f;this.j=d-this.va;break a}void 0!==b&&-1<b?(this.j=Math.max(b,d+1-this.va),this.X=void 0):this.j=Number.MAX_VALUE}if(!e&&this.X&&"g"in this.X)throw Error('Unexpected "g" flag in sparse object of message that is not a group type.');if(c){b=h&&!g&&!0;e=this.j;var t;for(h=0;h<c.length;h++)g=c[h],g<e?(g+=this.va,(d=a[g])?ke(d,b):a[g]=Ed):(t||(t=Rd(this)),(d=t[g])?ke(d,b):t[g]=Ed)}}
H.prototype.toJSON=function(){var a=this.C,b;Dd?b=a:b=Nd(a,Od,Qd);return b};
function le(a){Dd=!0;try{return JSON.stringify(a.toJSON(),me)}finally{Dd=!1}}
H.prototype.clone=function(){var a=Nd(this.C,Pd,zd);yd(a);Id=a;a=new this.constructor(a);Id=void 0;ne(a,this);return a};
function ke(a,b){if(Array.isArray(a)){var c=qd(a),d=1;!b||c&2||(d|=16);(c&d)!==d&&rd(a,c|d)}}
H.prototype.jb=Bd;H.prototype.toString=function(){return this.C.toString()};
function me(a,b){return Ld(b)}
function ne(a,b){b.Ma&&(a.Ma=b.Ma.slice());var c=b.h;if(c){b=b.X;for(var d in c){var e=c[d];if(e){var f=!(!b||!b[d]),g=+d;if(Array.isArray(e)){if(e.length)for(f=ae(a,e[0].constructor,g,f),g=0;g<Math.min(f.length,e.length);g++)ne(f[g],e[g])}else throw Error("unexpected object: type: "+Qa(e)+": "+e);}}}}
;function oe(a){var b=this.h,c=this.i;return this.isRepeated?ae(a,b,c,!0):Yd(a,b,c,!0)}
;function pe(a){this.Tb=a}
;function qe(a,b,c){this.i=a;this.l=b;this.h=c||[];this.Aa=new Map}
k=qe.prototype;k.Ec=function(a){var b=Ka.apply(1,arguments),c=this.ub(b);c?c.push(new pe(a)):this.qc(a,b)};
k.qc=function(a){this.Aa.set(this.Zb(Ka.apply(1,arguments)),[new pe(a)])};
k.ub=function(){var a=this.Zb(Ka.apply(0,arguments));return this.Aa.has(a)?this.Aa.get(a):void 0};
k.Qc=function(){var a=this.ub(Ka.apply(0,arguments));return a&&a.length?a[0]:void 0};
k.clear=function(){this.Aa.clear()};
k.Zb=function(){var a=Ka.apply(0,arguments);return a?a.join(","):"key"};function re(a,b){qe.call(this,a,3,b)}
u(re,qe);re.prototype.j=function(a){var b=Ka.apply(1,arguments),c=0,d=this.Qc(b);d&&(c=d.Tb);this.qc(c+a,b)};function se(a,b){qe.call(this,a,2,b)}
u(se,qe);se.prototype.j=function(a){this.Ec(a,Ka.apply(1,arguments))};function te(a){a&&"function"==typeof a.dispose&&a.dispose()}
;function ue(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];Ra(d)?ue.apply(null,d):te(d)}}
;function J(){this.M=this.M;this.v=this.v}
J.prototype.M=!1;J.prototype.h=function(){return this.M};
J.prototype.dispose=function(){this.M||(this.M=!0,this.B())};
function ve(a,b){we(a,$a(te,b))}
function we(a,b){a.M?b():(a.v||(a.v=[]),a.v.push(b))}
J.prototype.B=function(){if(this.v)for(;this.v.length;)this.v.shift()()};function xe(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
xe.prototype.stopPropagation=function(){this.j=!0};
xe.prototype.preventDefault=function(){this.defaultPrevented=!0};function ye(a){var b=B("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(g){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||y.$googDebugFname||b}catch(g){e="Not available",c=!0}b=ze(a);if(!(!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){c=a.message;if(null==
c){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)c=a.constructor.name;else if(c=a.constructor,Ae[c])c=Ae[c];else{c=String(c);if(!Ae[c]){var f=/function\s+([^\(]+)/m.exec(c);Ae[c]=f?f[1]:"[Anonymous]"}c=Ae[c]}c='Unknown Error of type "'+c+'"'}else c="Unknown Error of unknown type";"function"===typeof a.toString&&Object.prototype.toString!==a.toString&&(c+=": "+a.toString())}return{message:c,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:b||"Not available"}}a.stack=
b;return{message:a.message,name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:a.stack}}
function ze(a,b){b||(b={});b[Be(a)]=!0;var c=a.stack||"";(a=a.cause)&&!b[Be(a)]&&(c+="\nCaused by: ",a.stack&&0==a.stack.indexOf(a.toString())||(c+="string"===typeof a?a:a.message+"\n"),c+=ze(a,b));return c}
function Be(a){var b="";"function"===typeof a.toString&&(b=""+a);return b+a.stack}
var Ae={};var Ce=function(){if(!y.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});
try{y.addEventListener("test",function(){},b),y.removeEventListener("test",function(){},b)}catch(c){}return a}();function De(a,b){xe.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
ab(De,xe);var Ee={2:"touch",3:"pen",4:"mouse"};
De.prototype.init=function(a,b){var c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;if(b=a.relatedTarget){if(Mc){a:{try{Ic(b.nodeName);var e=!0;break a}catch(f){}e=!1}e||(b=null)}}else"mouseover"==c?b=a.fromElement:"mouseout"==c&&(b=a.toElement);this.relatedTarget=b;d?(this.clientX=void 0!==d.clientX?d.clientX:d.pageX,this.clientY=void 0!==d.clientY?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||
0):(this.clientX=void 0!==a.clientX?a.clientX:a.pageX,this.clientY=void 0!==a.clientY?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||("keypress"==c?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType="string"===typeof a.pointerType?a.pointerType:Ee[a.pointerType]||"";this.state=a.state;
this.i=a;a.defaultPrevented&&De.Y.preventDefault.call(this)};
De.prototype.stopPropagation=function(){De.Y.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
De.prototype.preventDefault=function(){De.Y.preventDefault.call(this);var a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var Fe="closure_listenable_"+(1E6*Math.random()|0);var Ge=0;function Me(a,b,c,d,e){this.listener=a;this.proxy=null;this.src=b;this.type=c;this.capture=!!d;this.hb=e;this.key=++Ge;this.Oa=this.cb=!1}
function Ne(a){a.Oa=!0;a.listener=null;a.proxy=null;a.src=null;a.hb=null}
;function Oe(a){this.src=a;this.listeners={};this.h=0}
Oe.prototype.add=function(a,b,c,d,e){var f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);var g=Pe(a,b,d,e);-1<g?(b=a[g],c||(b.cb=!1)):(b=new Me(b,this.src,f,!!d,e),b.cb=c,a.push(b));return b};
Oe.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;var e=this.listeners[a];b=Pe(e,b,c,d);return-1<b?(Ne(e[b]),Array.prototype.splice.call(e,b,1),0==e.length&&(delete this.listeners[a],this.h--),!0):!1};
function Qe(a,b){var c=b.type;c in a.listeners&&mb(a.listeners[c],b)&&(Ne(b),0==a.listeners[c].length&&(delete a.listeners[c],a.h--))}
function Pe(a,b,c,d){for(var e=0;e<a.length;++e){var f=a[e];if(!f.Oa&&f.listener==b&&f.capture==!!c&&f.hb==d)return e}return-1}
;var Re="closure_lm_"+(1E6*Math.random()|0),Se={},Te=0;function Ue(a,b,c,d,e){if(d&&d.once)Ve(a,b,c,d,e);else if(Array.isArray(b))for(var f=0;f<b.length;f++)Ue(a,b[f],c,d,e);else c=We(c),a&&a[Fe]?a.ia(b,c,Sa(d)?!!d.capture:!!d,e):Xe(a,b,c,!1,d,e)}
function Xe(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");var g=Sa(e)?!!e.capture:!!e,h=Ye(a);h||(a[Re]=h=new Oe(a));c=h.add(b,c,d,g,f);if(!c.proxy){d=Ze();c.proxy=d;d.src=a;d.listener=c;if(a.addEventListener)Ce||(e=g),void 0===e&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent($e(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");Te++}}
function Ze(){function a(c){return b.call(a.src,a.listener,c)}
var b=af;return a}
function Ve(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)Ve(a,b[f],c,d,e);else c=We(c),a&&a[Fe]?a.l.add(String(b),c,!0,Sa(d)?!!d.capture:!!d,e):Xe(a,b,c,!0,d,e)}
function bf(a,b,c,d,e){if(Array.isArray(b))for(var f=0;f<b.length;f++)bf(a,b[f],c,d,e);else(d=Sa(d)?!!d.capture:!!d,c=We(c),a&&a[Fe])?a.l.remove(String(b),c,d,e):a&&(a=Ye(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=Pe(b,c,d,e)),(c=-1<a?b[a]:null)&&cf(c))}
function cf(a){if("number"!==typeof a&&a&&!a.Oa){var b=a.src;if(b&&b[Fe])Qe(b.l,a);else{var c=a.type,d=a.proxy;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent($e(c),d):b.addListener&&b.removeListener&&b.removeListener(d);Te--;(c=Ye(b))?(Qe(c,a),0==c.h&&(c.src=null,b[Re]=null)):Ne(a)}}}
function $e(a){return a in Se?Se[a]:Se[a]="on"+a}
function af(a,b){if(a.Oa)a=!0;else{b=new De(b,this);var c=a.listener,d=a.hb||a.src;a.cb&&cf(a);a=c.call(d,b)}return a}
function Ye(a){a=a[Re];return a instanceof Oe?a:null}
var df="__closure_events_fn_"+(1E9*Math.random()>>>0);function We(a){if("function"===typeof a)return a;a[df]||(a[df]=function(b){return a.handleEvent(b)});
return a[df]}
;function ef(){J.call(this);this.l=new Oe(this);this.Bc=this;this.ka=null}
ab(ef,J);ef.prototype[Fe]=!0;ef.prototype.addEventListener=function(a,b,c,d){Ue(this,a,b,c,d)};
ef.prototype.removeEventListener=function(a,b,c,d){bf(this,a,b,c,d)};
function ff(a,b){var c=a.ka;if(c){var d=[];for(var e=1;c;c=c.ka)d.push(c),++e}a=a.Bc;c=b.type||b;"string"===typeof b?b=new xe(b,a):b instanceof xe?b.target=b.target||a:(e=b,b=new xe(c,a),zb(b,e));e=!0;if(d)for(var f=d.length-1;!b.j&&0<=f;f--){var g=b.h=d[f];e=gf(g,c,!0,b)&&e}b.j||(g=b.h=a,e=gf(g,c,!0,b)&&e,b.j||(e=gf(g,c,!1,b)&&e));if(d)for(f=0;!b.j&&f<d.length;f++)g=b.h=d[f],e=gf(g,c,!1,b)&&e}
ef.prototype.B=function(){ef.Y.B.call(this);if(this.l){var a=this.l,b=0,c;for(c in a.listeners){for(var d=a.listeners[c],e=0;e<d.length;e++)++b,Ne(d[e]);delete a.listeners[c];a.h--}}this.ka=null};
ef.prototype.ia=function(a,b,c,d){return this.l.add(String(a),b,!1,c,d)};
function gf(a,b,c,d){b=a.l.listeners[String(b)];if(!b)return!0;b=b.concat();for(var e=!0,f=0;f<b.length;++f){var g=b[f];if(g&&!g.Oa&&g.capture==c){var h=g.listener,l=g.hb||g.src;g.cb&&Qe(a.l,g);e=!1!==h.call(l,d)&&e}}return e&&!d.defaultPrevented}
;function hf(a,b){this.j=a;this.l=b;this.i=0;this.h=null}
hf.prototype.get=function(){if(0<this.i){this.i--;var a=this.h;this.h=a.next;a.next=null}else a=this.j();return a};
function jf(a,b){a.l(b);100>a.i&&(a.i++,b.next=a.h,a.h=b)}
;function kf(a,b){return a+Math.random()*(b-a)}
;function lf(a,b){this.x=void 0!==a?a:0;this.y=void 0!==b?b:0}
k=lf.prototype;k.clone=function(){return new lf(this.x,this.y)};
k.equals=function(a){return a instanceof lf&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
k.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
k.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
k.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};
k.scale=function(a,b){this.x*=a;this.y*="number"===typeof b?b:a;return this};function mf(a,b){this.width=a;this.height=b}
k=mf.prototype;k.clone=function(){return new mf(this.width,this.height)};
k.aspectRatio=function(){return this.width/this.height};
k.Na=function(){return!(this.width*this.height)};
k.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
k.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
k.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};
k.scale=function(a,b){this.width*=a;this.height*="number"===typeof b?b:a;return this};function nf(a){var b=document;return"string"===typeof a?b.getElementById(a):a}
function of(a){var b=document;a=String(a);"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());return b.createElement(a)}
function pf(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var qf;function rf(){var a=y.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!C("Presto")&&(a=function(){var e=of("IFRAME");e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=Za(function(l){if(("*"==h||l.origin==h)&&l.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!Vb()){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.Sb;c.Sb=null;e()}};
return function(e){d.next={Sb:e};d=d.next;b.port2.postMessage(0)}}return function(e){y.setTimeout(e,0)}}
;function sf(){this.i=this.h=null}
sf.prototype.add=function(a,b){var c=tf.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c};
sf.prototype.remove=function(){var a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a};
var tf=new hf(function(){return new uf},function(a){return a.reset()});
function uf(){this.next=this.scope=this.h=null}
uf.prototype.set=function(a,b){this.h=a;this.scope=b;this.next=null};
uf.prototype.reset=function(){this.next=this.scope=this.h=null};var vf,wf=!1,xf=new sf;function yf(a,b){vf||zf();wf||(vf(),wf=!0);xf.add(a,b)}
function zf(){if(y.Promise&&y.Promise.resolve){var a=y.Promise.resolve(void 0);vf=function(){a.then(Af)}}else vf=function(){var b=Af;
"function"!==typeof y.setImmediate||y.Window&&y.Window.prototype&&!C("Edge")&&y.Window.prototype.setImmediate==y.setImmediate?(qf||(qf=rf()),qf(b)):y.setImmediate(b)}}
function Af(){for(var a;a=xf.remove();){try{a.h.call(a.scope)}catch(b){Fc(b)}jf(tf,a)}wf=!1}
;function Bf(a){this.h=0;this.v=void 0;this.l=this.i=this.j=null;this.m=this.o=!1;if(a!=eb)try{var b=this;a.call(void 0,function(c){Cf(b,2,c)},function(c){Cf(b,3,c)})}catch(c){Cf(this,3,c)}}
function Df(){this.next=this.context=this.i=this.j=this.h=null;this.l=!1}
Df.prototype.reset=function(){this.context=this.i=this.j=this.h=null;this.l=!1};
var Ef=new hf(function(){return new Df},function(a){a.reset()});
function Ff(a,b,c){var d=Ef.get();d.j=a;d.i=b;d.context=c;return d}
function Gf(a){return new Bf(function(b,c){c(a)})}
Bf.prototype.then=function(a,b,c){return Hf(this,"function"===typeof a?a:null,"function"===typeof b?b:null,c)};
Bf.prototype.$goog_Thenable=!0;k=Bf.prototype;k.qb=function(a,b){return Hf(this,null,a,b)};
k.catch=Bf.prototype.qb;k.cancel=function(a){if(0==this.h){var b=new If(a);yf(function(){Jf(this,b)},this)}};
function Jf(a,b){if(0==a.h)if(a.j){var c=a.j;if(c.i){for(var d=0,e=null,f=null,g=c.i;g&&(g.l||(d++,g.h==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.h&&1==d?Jf(c,b):(f?(d=f,d.next==c.l&&(c.l=d),d.next=d.next.next):Kf(c),Lf(c,e,3,b)))}a.j=null}else Cf(a,3,b)}
function Mf(a,b){a.i||2!=a.h&&3!=a.h||Nf(a);a.l?a.l.next=b:a.i=b;a.l=b}
function Hf(a,b,c,d){var e=Ff(null,null,null);e.h=new Bf(function(f,g){e.j=b?function(h){try{var l=b.call(d,h);f(l)}catch(m){g(m)}}:f;
e.i=c?function(h){try{var l=c.call(d,h);void 0===l&&h instanceof If?g(h):f(l)}catch(m){g(m)}}:g});
e.h.j=a;Mf(a,e);return e.h}
k.zd=function(a){this.h=0;Cf(this,2,a)};
k.Ad=function(a){this.h=0;Cf(this,3,a)};
function Cf(a,b,c){if(0==a.h){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.h=1;a:{var d=c,e=a.zd,f=a.Ad;if(d instanceof Bf){Mf(d,Ff(e||eb,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(m){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Sa(d))try{var l=d.then;if("function"===typeof l){Of(d,l,e,f,a);g=!0;break a}}catch(m){f.call(a,m);g=!0;break a}g=!1}}}g||(a.v=c,a.h=b,a.j=null,Nf(a),3!=b||c instanceof If||Pf(a,c))}}
function Of(a,b,c,d,e){function f(l){h||(h=!0,d.call(e,l))}
function g(l){h||(h=!0,c.call(e,l))}
var h=!1;try{b.call(a,g,f)}catch(l){f(l)}}
function Nf(a){a.o||(a.o=!0,yf(a.Oc,a))}
function Kf(a){var b=null;a.i&&(b=a.i,a.i=b.next,b.next=null);a.i||(a.l=null);return b}
k.Oc=function(){for(var a;a=Kf(this);)Lf(this,a,this.h,this.v);this.o=!1};
function Lf(a,b,c,d){if(3==c&&b.i&&!b.l)for(;a&&a.m;a=a.j)a.m=!1;if(b.h)b.h.j=null,Qf(b,c,d);else try{b.l?b.j.call(b.context):Qf(b,c,d)}catch(e){Rf.call(null,e)}jf(Ef,b)}
function Qf(a,b,c){2==b?a.j.call(a.context,c):a.i&&a.i.call(a.context,c)}
function Pf(a,b){a.m=!0;yf(function(){a.m&&Rf.call(null,b)})}
var Rf=Fc;function If(a){cb.call(this,a)}
ab(If,cb);If.prototype.name="cancel";function Sf(a,b){ef.call(this);this.j=a||1;this.i=b||y;this.m=Za(this.xd,this);this.o=Date.now()}
ab(Sf,ef);k=Sf.prototype;k.enabled=!1;k.aa=null;function Tf(a,b){a.j=b;a.aa&&a.enabled?(a.stop(),a.start()):a.aa&&a.stop()}
k.xd=function(){if(this.enabled){var a=Date.now()-this.o;0<a&&a<.8*this.j?this.aa=this.i.setTimeout(this.m,this.j-a):(this.aa&&(this.i.clearTimeout(this.aa),this.aa=null),ff(this,"tick"),this.enabled&&(this.stop(),this.start()))}};
k.start=function(){this.enabled=!0;this.aa||(this.aa=this.i.setTimeout(this.m,this.j),this.o=Date.now())};
k.stop=function(){this.enabled=!1;this.aa&&(this.i.clearTimeout(this.aa),this.aa=null)};
k.B=function(){Sf.Y.B.call(this);this.stop();delete this.i};
function Uf(a,b,c){if("function"===typeof a)c&&(a=Za(a,c));else if(a&&"function"==typeof a.handleEvent)a=Za(a.handleEvent,a);else throw Error("Invalid listener argument");return 2147483647<Number(b)?-1:y.setTimeout(a,b||0)}
;function Vf(a){this.v=a;this.h=new Map;this.o=new Set;this.j=0;this.l=100;this.flushInterval=3E4;this.i=new Sf(this.flushInterval);this.i.ia("tick",this.sb,!1,this);this.m=!1}
k=Vf.prototype;k.sendIsolatedPayload=function(a){this.m=a;this.l=1};
function Wf(a){a.i.enabled||a.i.start();a.j++;a.j>=a.l&&a.sb()}
k.sb=function(){var a=this.h.values();a=[].concat(ja(a)).filter(function(b){return b.Aa.size});
a.length&&this.v.flush(a,this.m);Xf(a);this.j=0;this.i.enabled&&this.i.stop()};
k.Pb=function(a){var b=Ka.apply(1,arguments);this.h.has(a)||this.h.set(a,new re(a,b))};
k.Qb=function(a){var b=Ka.apply(1,arguments);this.h.has(a)||this.h.set(a,new se(a,b))};
function Yf(a,b){return a.o.has(b)?void 0:a.h.get(b)}
k.Wa=function(a){this.zc.apply(this,[a,1].concat(ja(Ka.apply(1,arguments))))};
k.zc=function(a,b){var c=Ka.apply(2,arguments),d=Yf(this,a);d&&d instanceof re&&(d.j(b,c),Wf(this))};
k.rb=function(a,b){var c=Ka.apply(2,arguments),d=Yf(this,a);d&&d instanceof se&&(d.j(b,c),Wf(this))};
function Xf(a){for(var b=0;b<a.length;b++)a[b].clear()}
;function Zf(a){this.h=a;this.h.Pb("/client_streamz/bg/fiec",{La:3,Ka:"rk"},{La:2,Ka:"ec"})}
function $f(a){this.h=a;this.h.Qb("/client_streamz/bg/fil",{La:3,Ka:"rk"})}
function ag(a){this.h=a;this.h.Pb("/client_streamz/bg/fsc",{La:3,Ka:"rk"})}
function bg(a){this.h=a;this.h.Qb("/client_streamz/bg/fsl",{La:3,Ka:"rk"})}
;function cg(a){H.call(this,a,-1,dg)}
u(cg,H);function eg(a){H.call(this,a,-1,fg)}
u(eg,H);function gg(a){H.call(this,a)}
u(gg,H);function hg(a){H.call(this,a)}
u(hg,H);var dg=[3,6,4],fg=[1],ig=[1,2,3],jg=[1,2,3];function kg(a){H.call(this,a,-1,lg)}
u(kg,H);var lg=[1];function mg(a){if(!a)return"";if(/^about:(?:blank|srcdoc)$/.test(a))return window.origin||"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if("http"!==c&&"https"!==c&&"chrome-extension"!==c&&"moz-extension"!==c&&"file"!==c&&"android-app"!==
c&&"chrome-search"!==c&&"chrome-untrusted"!==c&&"chrome"!==c&&"app"!==c&&"devtools"!==c)throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===c&&"80"!==e||"https"===c&&"443"!==e)a=":"+e}return c+"://"+b+a}
;function ng(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;q=m=0}
function b(r){for(var w=g,t=0;64>t;t+=4)w[t/4]=r[t]<<24|r[t+1]<<16|r[t+2]<<8|r[t+3];for(t=16;80>t;t++)r=w[t-3]^w[t-8]^w[t-14]^w[t-16],w[t]=(r<<1|r>>>31)&4294967295;r=e[0];var A=e[1],E=e[2],F=e[3],O=e[4];for(t=0;80>t;t++){if(40>t)if(20>t){var N=F^A&(E^F);var R=1518500249}else N=A^E^F,R=1859775393;else 60>t?(N=A&E|F&(A|E),R=2400959708):(N=A^E^F,R=3395469782);N=((r<<5|r>>>27)&4294967295)+N+O+R+w[t]&4294967295;O=F;F=E;E=(A<<30|A>>>2)&4294967295;A=r;r=N}e[0]=e[0]+r&4294967295;e[1]=e[1]+A&4294967295;e[2]=
e[2]+E&4294967295;e[3]=e[3]+F&4294967295;e[4]=e[4]+O&4294967295}
function c(r,w){if("string"===typeof r){r=unescape(encodeURIComponent(r));for(var t=[],A=0,E=r.length;A<E;++A)t.push(r.charCodeAt(A));r=t}w||(w=r.length);t=0;if(0==m)for(;t+64<w;)b(r.slice(t,t+64)),t+=64,q+=64;for(;t<w;)if(f[m++]=r[t++],q++,64==m)for(m=0,b(f);t+64<w;)b(r.slice(t,t+64)),t+=64,q+=64}
function d(){var r=[],w=8*q;56>m?c(h,56-m):c(h,64-(m-56));for(var t=63;56<=t;t--)f[t]=w&255,w>>>=8;b(f);for(t=w=0;5>t;t++)for(var A=24;0<=A;A-=8)r[w++]=e[t]>>A&255;return r}
for(var e=[],f=[],g=[],h=[128],l=1;64>l;++l)h[l]=0;var m,q;a();return{reset:a,update:c,digest:d,Lc:function(){for(var r=d(),w="",t=0;t<r.length;t++)w+="0123456789ABCDEF".charAt(Math.floor(r[t]/16))+"0123456789ABCDEF".charAt(r[t]%16);return w}}}
;function og(a,b,c){var d=String(y.location.href);return d&&a&&b?[b,pg(mg(d),a,c||null)].join(" "):null}
function pg(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],hb(d,function(h){e.push(h)}),qg(e.join(" "));
var f=[],g=[];hb(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];hb(d,function(h){e.push(h)});
a=qg(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function qg(a){var b=ng();b.update(a);return b.Lc().toLowerCase()}
;var rg={};function sg(a){this.h=a||{cookie:""}}
k=sg.prototype;k.isEnabled=function(){if(!y.navigator.cookieEnabled)return!1;if(!this.Na())return!0;this.set("TESTCOOKIESENABLED","1",{ib:60});if("1"!==this.get("TESTCOOKIESENABLED"))return!1;this.remove("TESTCOOKIESENABLED");return!0};
k.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Or;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.ib}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+1E3*h)).toUTCString();this.h.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+
e:"")};
k.get=function(a,b){for(var c=a+"=",d=(this.h.cookie||"").split(";"),e=0,f;e<d.length;e++){f=Nb(d[e]);if(0==f.lastIndexOf(c,0))return f.slice(c.length);if(f==a)return""}return b};
k.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{ib:0,path:b,domain:c});return d};
k.xb=function(){return tg(this).keys};
k.Na=function(){return!this.h.cookie};
k.clear=function(){for(var a=tg(this).keys,b=a.length-1;0<=b;b--)this.remove(a[b])};
function tg(a){a=(a.h.cookie||"").split(";");for(var b=[],c=[],d,e,f=0;f<a.length;f++)e=Nb(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));return{keys:b,values:c}}
var ug=new sg("undefined"==typeof document?null:document);function vg(a){return!!rg.FPA_SAMESITE_PHASE2_MOD||!(void 0===a||!a)}
function wg(a){a=void 0===a?!1:a;var b=y.__SAPISID||y.__APISID||y.__3PSAPISID||y.__OVERRIDE_SID;vg(a)&&(b=b||y.__1PSAPISID);if(b)return!0;var c=new sg(document);b=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID");vg(a)&&(b=b||c.get("__Secure-1PAPISID"));return!!b}
function xg(a,b,c,d){(a=y[a])||(a=(new sg(document)).get(b));return a?og(a,c,d):null}
function yg(a,b){b=void 0===b?!1:b;var c=mg(String(y.location.href)),d=[];if(wg(b)){c=0==c.indexOf("https:")||0==c.indexOf("chrome-extension:")||0==c.indexOf("moz-extension:");var e=c?y.__SAPISID:y.__APISID;e||(e=new sg(document),e=e.get(c?"SAPISID":"APISID")||e.get("__Secure-3PAPISID"));(e=e?og(e,c?"SAPISIDHASH":"APISIDHASH",a):null)&&d.push(e);c&&vg(b)&&((b=xg("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&d.push(b),(a=xg("__3PSAPISID","__Secure-3PAPISID","SAPISID3PHASH",a))&&d.push(a))}return 0==
d.length?null:d.join(" ")}
;function zg(a){H.call(this,a,-1,Ag)}
u(zg,H);var Ag=[2];function Bg(a){this.h=this.i=this.j=a}
Bg.prototype.reset=function(){this.h=this.i=this.j};
Bg.prototype.getValue=function(){return this.i};function Cg(a){var b=[];Dg(new Eg,a,b);return b.join("")}
function Eg(){}
function Dg(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),Dg(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],"function"!=typeof f&&(c.push(e),Fg(d,c),c.push(":"),Dg(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Fg(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Gg={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\v":"\\u000b"},Hg=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Fg(a,b){b.push('"',a.replace(Hg,function(c){var d=Gg[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).slice(1),Gg[c]=d);return d}),'"')}
;function Ig(){}
Ig.prototype.h=null;Ig.prototype.getOptions=function(){var a;(a=this.h)||(a={},Jg(this)&&(a[0]=!0,a[1]=!0),a=this.h=a);return a};var Kg;function Lg(){}
ab(Lg,Ig);function Mg(a){return(a=Jg(a))?new ActiveXObject(a):new XMLHttpRequest}
function Jg(a){if(!a.i&&"undefined"==typeof XMLHttpRequest&&"undefined"!=typeof ActiveXObject){for(var b=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"],c=0;c<b.length;c++){var d=b[c];try{return new ActiveXObject(d),a.i=d}catch(e){}}throw Error("Could not create ActiveXObject. ActiveX might be disabled, or MSXML might not be installed");}return a.i}
Kg=new Lg;function Ng(a){ef.call(this);this.headers=new Map;this.K=a||null;this.i=!1;this.I=this.A=null;this.m=this.T="";this.j=this.P=this.s=this.O=!1;this.o=0;this.F=null;this.ca="";this.V=this.W=!1}
ab(Ng,ef);var Og=/^https?$/i,Pg=["POST","PUT"],Qg=[];function Rg(a,b,c,d,e,f,g){var h=new Ng;Qg.push(h);b&&h.ia("complete",b);h.l.add("ready",h.Jc,!0,void 0,void 0);f&&(h.o=Math.max(0,f));g&&(h.W=g);h.send(a,c,d,e)}
k=Ng.prototype;k.Jc=function(){this.dispose();mb(Qg,this)};
k.send=function(a,b,c,d){if(this.A)throw Error("[goog.net.XhrIo] Object is active with another request="+this.T+"; newUri="+a);b=b?b.toUpperCase():"GET";this.T=a;this.m="";this.O=!1;this.i=!0;this.A=this.K?Mg(this.K):Mg(Kg);this.I=this.K?this.K.getOptions():Kg.getOptions();this.A.onreadystatechange=Za(this.ic,this);try{this.getStatus(),this.P=!0,this.A.open(b,String(a),!0),this.P=!1}catch(g){this.getStatus();Sg(this,g);return}a=c||"";c=new Map(this.headers);if(d)if(Object.getPrototypeOf(d)===Object.prototype)for(var e in d)c.set(e,
d[e]);else if("function"===typeof d.keys&&"function"===typeof d.get){e=p(d.keys());for(var f=e.next();!f.done;f=e.next())f=f.value,c.set(f,d.get(f))}else throw Error("Unknown input type for opt_headers: "+String(d));d=Array.from(c.keys()).find(function(g){return"content-type"==g.toLowerCase()});
e=y.FormData&&a instanceof y.FormData;!(0<=gb(Pg,b))||d||e||c.set("Content-Type","application/x-www-form-urlencoded;charset=utf-8");b=p(c);for(d=b.next();!d.done;d=b.next())c=p(d.value),d=c.next().value,c=c.next().value,this.A.setRequestHeader(d,c);this.ca&&(this.A.responseType=this.ca);"withCredentials"in this.A&&this.A.withCredentials!==this.W&&(this.A.withCredentials=this.W);try{Tg(this),0<this.o&&(this.V=Ug(this.A),this.getStatus(),this.V?(this.A.timeout=this.o,this.A.ontimeout=Za(this.uc,this)):
this.F=Uf(this.uc,this.o,this)),this.getStatus(),this.s=!0,this.A.send(a),this.s=!1}catch(g){this.getStatus(),Sg(this,g)}};
function Ug(a){return Kc&&"number"===typeof a.timeout&&void 0!==a.ontimeout}
k.uc=function(){"undefined"!=typeof Oa&&this.A&&(this.m="Timed out after "+this.o+"ms, aborting",this.getStatus(),ff(this,"timeout"),this.abort(8))};
function Sg(a,b){a.i=!1;a.A&&(a.j=!0,a.A.abort(),a.j=!1);a.m=b;Vg(a);Wg(a)}
function Vg(a){a.O||(a.O=!0,ff(a,"complete"),ff(a,"error"))}
k.abort=function(){this.A&&this.i&&(this.getStatus(),this.i=!1,this.j=!0,this.A.abort(),this.j=!1,ff(this,"complete"),ff(this,"abort"),Wg(this))};
k.B=function(){this.A&&(this.i&&(this.i=!1,this.j=!0,this.A.abort(),this.j=!1),Wg(this,!0));Ng.Y.B.call(this)};
k.ic=function(){this.h()||(this.P||this.s||this.j?Zg(this):this.bd())};
k.bd=function(){Zg(this)};
function Zg(a){if(a.i&&"undefined"!=typeof Oa)if(a.I[1]&&4==$g(a)&&2==a.getStatus())a.getStatus();else if(a.s&&4==$g(a))Uf(a.ic,0,a);else if(ff(a,"readystatechange"),a.isComplete()){a.getStatus();a.i=!1;try{if(ah(a))ff(a,"complete"),ff(a,"success");else{try{var b=2<$g(a)?a.A.statusText:""}catch(c){b=""}a.m=b+" ["+a.getStatus()+"]";Vg(a)}}finally{Wg(a)}}}
function Wg(a,b){if(a.A){Tg(a);var c=a.A,d=a.I[0]?function(){}:null;
a.A=null;a.I=null;b||ff(a,"ready");try{c.onreadystatechange=d}catch(e){}}}
function Tg(a){a.A&&a.V&&(a.A.ontimeout=null);a.F&&(y.clearTimeout(a.F),a.F=null)}
k.isActive=function(){return!!this.A};
k.isComplete=function(){return 4==$g(this)};
function ah(a){var b=a.getStatus();a:switch(b){case 200:case 201:case 202:case 204:case 206:case 304:case 1223:var c=!0;break a;default:c=!1}if(!c){if(b=0===b)a=oc(1,String(a.T)),!a&&y.self&&y.self.location&&(a=y.self.location.protocol.slice(0,-1)),b=!Og.test(a?a.toLowerCase():"");c=b}return c}
function $g(a){return a.A?a.A.readyState:0}
k.getStatus=function(){try{return 2<$g(this)?this.A.status:-1}catch(a){return-1}};
k.getLastError=function(){return"string"===typeof this.m?this.m:String(this.m)};function bh(a){H.call(this,a)}
u(bh,H);function ch(a){H.call(this,a,-1,dh)}
u(ch,H);var dh=[1];var eh=["platform","platformVersion","architecture","model","uaFullVersion"];new ch;function fh(a){H.call(this,a)}
u(fh,H);function gh(a){H.call(this,a,31,hh)}
u(gh,H);var hh=[3,20,27];function ih(a){H.call(this,a,17,jh)}
u(ih,H);var jh=[3,5];function kh(a){H.call(this,a,6,lh)}
u(kh,H);var lh=[5];function mh(a){H.call(this,a)}
u(mh,H);var nh;nh=new function(a,b,c){this.i=a;this.fieldName=b;this.h=c;this.isRepeated=0;this.j=oe}(175237375,{Er:0},mh);function oh(a,b,c,d,e,f,g,h,l,m,q){ef.call(this);var r=this;this.O="";this.j=[];this.Nb="";this.Ob=this.ta=-1;this.Ya=!1;this.I=this.m=null;this.F=0;this.Cc=1;this.timeoutMillis=0;this.ca=!1;ef.call(this);this.Za=b||function(){};
this.s=new ph(a,f);this.Ac=d;this.Xa=q;this.Dc=$a(kf,0,1);this.T=e||null;this.K=c||null;this.V=g||!1;this.pageId=l||null;this.logger=null;this.withCredentials=!h;this.Ha=f||!1;!this.Ha&&(65<=dc("Chromium")||45<=dc("Firefox")||12<=dc("Safari")||(Gc()||C("iPad")||C("iPod"))&&Hc());a=D(new fh,1,1);qh(this.s,a);this.o=new Bg(1E4);this.i=new Sf(this.o.getValue());ve(this,this.i);m=rh(this,m);Ue(this.i,"tick",m,!1,this);this.P=new Sf(6E5);ve(this,this.P);Ue(this.P,"tick",m,!1,this);this.V||this.P.start();
this.Ha||(Ue(document,"visibilitychange",function(){"hidden"===document.visibilityState&&r.W()}),Ue(document,"pagehide",this.W,!1,this))}
u(oh,ef);function rh(a,b){return b?function(){b().then(function(){a.flush()})}:function(){a.flush()}}
oh.prototype.B=function(){this.W();ef.prototype.B.call(this)};
function sh(a){a.T||(a.T=.01>a.Dc()?"https://www.google.com/log?format=json&hasfast=true":"https://play.google.com/log?format=json&hasfast=true");return a.T}
function th(a,b){a.o=new Bg(1>b?1:b);Tf(a.i,a.o.getValue())}
oh.prototype.log=function(a){a=a.clone();var b=this.Cc++;D(a,21,b);this.O&&D(a,26,this.O);if(!Sd(a,1)){b=a;var c=Date.now().toString();D(b,1,c)}null==Sd(a,15)&&D(a,15,60*(new Date).getTimezoneOffset());this.m&&(b=this.m.clone(),G(a,zg,16,b));for(;1E3<=this.j.length;)this.j.shift(),++this.F;this.j.push(a);ff(this,new uh(a));this.V||this.i.enabled||this.i.start()};
oh.prototype.flush=function(a,b){var c=this;if(0===this.j.length)a&&a();else if(this.ca)vh(this);else{var d=Date.now();if(this.Ob>d&&this.ta<d)b&&b("throttled");else{var e=wh(this.s,this.j,this.F);d={};var f=this.Za();f&&(d.Authorization=f);var g=sh(this);this.K&&(d["X-Goog-AuthUser"]=this.K,g=xc(g,"authuser",this.K));this.pageId&&(d["X-Goog-PageId"]=this.pageId,g=xc(g,"pageId",this.pageId));if(f&&this.Nb===f)b&&b("stale-auth-token");else{this.j=[];this.i.enabled&&this.i.stop();this.F=0;var h=le(e),
l;this.I&&this.I.isSupported(h.length)&&(l=this.I.compress(h));var m={url:g,body:h,Hc:1,Hb:d,requestType:"POST",withCredentials:this.withCredentials,timeoutMillis:this.timeoutMillis},q=function(t){c.o.reset();Tf(c.i,c.o.getValue());if(t){var A=null;try{var E=JSON.parse(t.replace(")]}'\n",""));A=new kh(E)}catch(F){}A&&(t=Number(fe(Sd(A,1),"-1")),0<t&&(c.ta=Date.now(),c.Ob=c.ta+t),A=nh.j(A))&&(A=fe(Sd(A,1),-1),-1!=A&&(c.Ya||th(c,A)))}a&&a()},r=function(t,A){var E=ae(e,gh,3),F=c.o;
F.h=Math.min(3E5,2*F.h);F.i=Math.min(3E5,F.h+Math.round(.2*(Math.random()-.5)*F.h));Tf(c.i,c.o.getValue());401===t&&f&&(c.Nb=f);void 0===A&&(A=500<=t&&600>t||401===t||0===t);A&&(c.j=E.concat(c.j),c.V||c.i.enabled||c.i.start());b&&b("net-send-failed",t)},w=function(){c.Xa?c.Xa.send(m,q,r):c.Ac(m,q,r)};
l?l.then(function(t){m.Hb["Content-Encoding"]="gzip";m.Hb["Content-Type"]="application/binary";m.body=t;m.Hc=2;w()},function(){w()}):w()}}}};
oh.prototype.W=function(){this.flush()};
function vh(a){xh(a,function(b,c){b=xc(b,"format","json");b=window.navigator.sendBeacon(b,le(c));a.ca&&!b&&(a.ca=!1);return b})}
function xh(a,b){if(0!==a.j.length){var c=Ec(sh(a),"format");c=vc(c,"auth",a.Za(),"authuser",a.K||"0");for(var d=0;10>d&&a.j.length;++d){var e=a.j.slice(0,32),f=wh(a.s,e,a.F);if(!b(c,f))break;a.F=0;a.j=a.j.slice(e.length)}a.i.enabled&&a.i.stop()}}
function uh(){xe.call(this,"event-logged",void 0)}
u(uh,xe);function ph(a,b){this.i=b=void 0===b?!1:b;this.uach=this.locale=null;this.h=new ih;D(this.h,2,a);b||(this.locale=document.documentElement.getAttribute("lang"));qh(this,new fh)}
function qh(a,b){G(a.h,fh,1,b);Sd(b,1)||D(b,1,1);a.i||(b=yh(a),Sd(b,5)||D(b,5,a.locale));a.uach&&(b=yh(a),Yd(b,ch,9)||G(b,ch,9,a.uach))}
function zh(a,b){var c=void 0===c?eh:c;b(window,c).then(function(d){a.uach=d;d=yh(a);G(d,ch,9,a.uach);return!0}).catch(function(){return!1})}
function yh(a){a=Yd(a.h,fh,1);var b=Yd(a,bh,11);b||(b=new bh,G(a,bh,11,b));return b}
function wh(a,b,c){c=void 0===c?0:c;a=a.h.clone();var d=Date.now().toString();a=D(a,4,d);b=ce(a,gh,3,b);c&&D(b,14,c);return b}
;function Ah(a,b,c){Rg(a.url,function(d){d=d.target;if(ah(d)){try{var e=d.A?d.A.responseText:""}catch(f){e=""}b(e)}else c(d.getStatus())},a.requestType,a.body,a.Hb,a.timeoutMillis,a.withCredentials)}
;function Bh(){this.j="https://play.google.com/log?format=json&hasfast=true";this.s=!1;this.m=Ah;this.h=""}
;function Ch(){var a=void 0===a?"":a;var b=void 0===b?"":b;var c=new Bh;c.h="";""!=a&&(c.j=a);b&&(c.i=b);a=new oh(1828,c.I?c.I:yg,"0",c.m,c.j,c.s,!1,c.P,void 0,void 0,c.o?c.o:void 0);c.M&&qh(a.s,c.M);if(c.i){b=c.i;var d=yh(a.s);D(d,7,b)}c.l&&(a.I=c.l);c.h&&(a.O=c.h);c.v&&((b=c.v)?(a.m||(a.m=new zg),b=le(b),D(a.m,4,b)):a.m&&D(a.m,4,void 0,!1));if(c.K){d=c.K;a.m||(a.m=new zg);b=a.m;if(null==d)d=Ed;else{var e=qd(d);1!==(e&1)&&(Object.isFrozen(d)&&(d=Array.prototype.slice.call(d)),rd(d,e|1))}D(b,2,d)}c.F&&
(b=c.F,a.Ya=!0,th(a,b));c.O&&zh(a.s,c.O);this.h=a}
Ch.prototype.flush=function(a){var b=a||[];if(b.length){a=new kg;for(var c=[],d=0;d<b.length;d++){var e=b[d],f=e,g=new cg;var h=D(g,1,f.i);var l=f;g=[];for(var m=0;m<l.h.length;m++)g.push(l.h[m].Ka);if(null==g)g=D(h,3,Ed);else{l=qd(g);if(!(l&4)){if(l&2||Object.isFrozen(g))g=Array.prototype.slice.call(g);for(m=0;m<g.length;m++)g[m]=g[m];rd(g,l|5)}g=D(h,3,g)}h=[];l=[];m=p(f.Aa.keys());for(var q=m.next();!q.done;q=m.next())l.push(q.value.split(","));for(m=0;m<l.length;m++){q=l[m];var r=f.l;for(var w=
f.ub(q)||[],t=[],A=0;A<w.length;A++){var E=w[A];E=E&&E.Tb;var F=new hg;switch(r){case 3:Wd(F,1,jg,Number(E));break;case 2:Wd(F,2,jg,Number(E))}t.push(F)}r=t;for(w=0;w<r.length;w++){t=r[w];A=new eg;t=G(A,hg,2,t);A=q;E=[];F=f;for(var O=[],N=0;N<F.h.length;N++)O.push(F.h[N].La);F=O;for(O=0;O<F.length;O++){N=F[O];var R=A[O],ca=new gg;switch(N){case 3:Wd(ca,1,ig,String(R));break;case 2:Wd(ca,2,ig,Number(R));break;case 1:Wd(ca,3,ig,"true"==R)}E.push(ca)}ce(t,gg,1,E);h.push(t)}}ce(g,eg,4,h);c.push(g);e.clear()}ce(a,
cg,1,c);b=this.h;a instanceof gh?b.log(a):(c=new gh,a=le(a),a=D(c,8,a),b.log(a));this.h.flush()}};function Dh(a){this.oa=a;this.v=Eh();this.m=new Ch;this.h=new Vf(this.m);this.o=new $f(this.h);this.j=new ag(this.h);this.l=new bg(this.h);this.i=new Zf(this.h)}
function Eh(){var a,b,c;return null!=(c=null==(a=globalThis.performance)?void 0:null==(b=a.now)?void 0:b.call(a))?c:Date.now()}
;function Fh(){var a=this;this.promise=new Promise(function(b,c){a.resolve=b;a.reject=c})}
;function Gh(a){var b=this;this.i=!1;var c=a.program;var d=a.Sc;if(a.fd){var e;this.ga=null!=(e=a.ga)?e:new Dh(d)}var f=new Fh;this.j=f.promise;if(!y[d]){var g;null!=(g=this.ga)&&g.i.h.Wa("/client_streamz/bg/fiec",g.oa,1)}else if(!y[d].a){var h;null!=(h=this.ga)&&h.i.h.Wa("/client_streamz/bg/fiec",h.oa,2)}this.l=p((0,y[d].a)(c,function(l,m){Promise.resolve().then(function(){var q;if(null!=(q=b.ga)){var r=Eh()-q.v;q.o.h.rb("/client_streamz/bg/fil",r,q.oa)}f.resolve({Fc:l,td:m})})},!0)).next().value;
this.sd=f.promise.then(function(){})}
Gh.prototype.snapshot=function(a){var b=this;if(this.i)throw Error("Already disposed");var c=Eh(),d;null!=(d=this.ga)&&d.j.h.Wa("/client_streamz/bg/fsc",d.oa);return this.j.then(function(e){var f=e.Fc;return new Promise(function(g){f(function(h){var l;if(null!=(l=b.ga)){var m=Eh()-c;l.l.h.rb("/client_streamz/bg/fsl",m,l.oa)}g(h)},[a.Vb,
a.ud])})})};
Gh.prototype.sc=function(a){if(this.i)throw Error("Already disposed");var b=Eh(),c;null!=(c=this.ga)&&c.j.h.Wa("/client_streamz/bg/fsc",c.oa);a=this.l([a.Vb,a.ud]);null!=(c=this.ga)&&(b=Eh()-b,c.l.h.rb("/client_streamz/bg/fsl",b,c.oa));return a};
Gh.prototype.dispose=function(){var a;null!=(a=this.ga)&&a.h.sb();this.i=!0;this.j.then(function(b){(b=b.td)&&b()})};
Gh.prototype.h=function(){return this.i};var Hh=window;Eb("csi.gstatic.com");Eb("googleads.g.doubleclick.net");Eb("partner.googleadservices.com");Eb("pubads.g.doubleclick.net");Eb("securepubads.g.doubleclick.net");Eb("tpc.googlesyndication.com");/*

 SPDX-License-Identifier: Apache-2.0
*/
var Ih;try{new URL("s://g"),Ih=!0}catch(a){Ih=!1}var Jh=Ih;var Kh={};function Lh(){}
function Mh(a){this.h=a}
u(Mh,Lh);Mh.prototype.toString=function(){return this.h};function Nh(a){var b="true".toString(),c=[new Mh(Oh[0].toLowerCase(),Kh)];if(0===c.length)throw Error("No prefixes are provided");if(c.map(function(d){if(d instanceof Mh)d=d.h;else throw Error("");return d}).every(function(d){return 0!=="data-loaded".indexOf(d)}))throw Error('Attribute "data-loaded" does not match any of the allowed prefixes.');
a.setAttribute("data-loaded",b)}
;function Ph(a,b){a.src=Lb(b);var c,d;(c=(b=null==(d=(c=(a.ownerDocument&&a.ownerDocument.defaultView||window).document).querySelector)?void 0:d.call(c,"script[nonce]"))?b.nonce||b.getAttribute("nonce")||"":"")&&a.setAttribute("nonce",c)}
;function Qh(a){this.Xc=a}
function Rh(a){return new Qh(function(b){return b.substr(0,a.length+1).toLowerCase()===a+":"})}
var Sh=[Rh("data"),Rh("http"),Rh("https"),Rh("mailto"),Rh("ftp"),new Qh(function(a){return/^[^:]*([/?#]|$)/.test(a)})];function Th(a){var b=Uh;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a(b[c],c,b)}
function Vh(){var a=[];Th(function(b){a.push(b)});
return a}
var Uh={Od:"allow-forms",Pd:"allow-modals",Qd:"allow-orientation-lock",Rd:"allow-pointer-lock",Sd:"allow-popups",Td:"allow-popups-to-escape-sandbox",Ud:"allow-presentation",Vd:"allow-same-origin",Wd:"allow-scripts",Xd:"allow-top-navigation",Yd:"allow-top-navigation-by-user-activation"},Wh=fb(function(){return Vh()});
function Xh(){var a=Yh(),b={};hb(Wh(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
function Yh(){var a=void 0===a?document:a;return a.createElement("iframe")}
;function Zh(a){"number"==typeof a&&(a=Math.round(a)+"px");return a}
;var $h=(new Date).getTime();var ai="client_dev_domain client_dev_regex_map client_dev_root_url client_rollout_override expflag forcedCapability jsfeat jsmode mods".split(" ");ja(ai);function bi(a){ef.call(this);var b=this;this.s=this.j=0;this.Z=null!=a?a:{S:function(e,f){return setTimeout(e,f)},
ea:function(e){clearTimeout(e)}};
var c,d;this.i=null!=(d=null==(c=window.navigator)?void 0:c.onLine)?d:!0;this.m=function(){return x(function(e){return v(e,ci(b),0)})};
window.addEventListener("offline",this.m);window.addEventListener("online",this.m);this.s||di(this)}
u(bi,ef);function ei(){var a=fi;bi.h||(bi.h=new bi(a));return bi.h}
bi.prototype.dispose=function(){window.removeEventListener("offline",this.m);window.removeEventListener("online",this.m);this.Z.ea(this.s);delete bi.h};
bi.prototype.U=function(){return this.i};
function di(a){a.s=a.Z.S(function(){var b;return x(function(c){if(1==c.h)return a.i?(null==(b=window.navigator)?0:b.onLine)?c.u(3):v(c,ci(a),3):v(c,ci(a),3);di(a);c.h=0})},3E4)}
function ci(a,b){return a.o?a.o:a.o=new Promise(function(c){var d,e,f,g;return x(function(h){switch(h.h){case 1:return d=window.AbortController?new window.AbortController:void 0,f=null==(e=d)?void 0:e.signal,g=!1,za(h,2,3),d&&(a.j=a.Z.S(function(){d.abort()},b||2E4)),v(h,fetch("/generate_204",{method:"HEAD",
signal:f}),5);case 5:g=!0;case 3:Ca(h);a.o=void 0;a.j&&(a.Z.ea(a.j),a.j=0);g!==a.i&&(a.i=g,a.i?ff(a,"networkstatus-online"):ff(a,"networkstatus-offline"));c(g);Da(h);break;case 2:Ba(h),g=!1,h.u(3)}})})}
;function gi(){this.data_=[];this.h=-1}
gi.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&Number.isInteger(a)&&this.data_[a]!==b&&(this.data_[a]=b,this.h=-1)};
gi.prototype.get=function(a){return!!this.data_[a]};
function hi(a){-1===a.h&&(a.h=kb(a.data_,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.h}
;function ii(a,b){this.h=a[y.Symbol.iterator]();this.i=b}
ii.prototype[Symbol.iterator]=function(){return this};
ii.prototype.next=function(){var a=this.h.next();return{value:a.done?void 0:this.i.call(void 0,a.value),done:a.done}};
function ji(a,b){return new ii(a,b)}
;function ki(){this.blockSize=-1}
;function li(){this.blockSize=-1;this.blockSize=64;this.h=[];this.m=[];this.o=[];this.j=[];this.j[0]=128;for(var a=1;a<this.blockSize;++a)this.j[a]=0;this.l=this.i=0;this.reset()}
ab(li,ki);li.prototype.reset=function(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.l=this.i=0};
function mi(a,b,c){c||(c=0);var d=a.o;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.h[0];c=a.h[1];var g=a.h[2],h=a.h[3],l=a.h[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var m=1518500249}else f=c^g^h,m=1859775393;else 60>e?(f=c&g|h&(c|g),m=2400959708):
(f=c^g^h,m=3395469782);f=(b<<5|b>>>27)+f+l+m+d[e]&4294967295;l=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+g&4294967295;a.h[3]=a.h[3]+h&4294967295;a.h[4]=a.h[4]+l&4294967295}
li.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.m,f=this.i;d<b;){if(0==f)for(;d<=c;)mi(this,a,d),d+=this.blockSize;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.blockSize){mi(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){mi(this,e);f=0;break}}this.i=f;this.l+=b}};
li.prototype.digest=function(){var a=[],b=8*this.l;56>this.i?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;56<=c;c--)this.m[c]=b&255,b/=256;mi(this,this.m);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.h[c]>>d&255,++b;return a};function ni(a){return"string"==typeof a.className?a.className:a.getAttribute&&a.getAttribute("class")||""}
function oi(a,b){"string"==typeof a.className?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function pi(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:ni(a).match(/\S+/g)||[],b=0<=gb(a,b));return b}
function qi(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):pi(a,"inverted-hdpi")&&oi(a,Array.prototype.filter.call(a.classList?a.classList:ni(a).match(/\S+/g)||[],function(b){return"inverted-hdpi"!=b}).join(" "))}
;function ri(){}
ri.prototype.next=function(){return si};
var si={done:!0,value:void 0};function ti(a){return{value:a,done:!1}}
ri.prototype.da=function(){return this};function ui(a){if(a instanceof vi||a instanceof wi||a instanceof xi)return a;if("function"==typeof a.next)return new vi(function(){return a});
if("function"==typeof a[Symbol.iterator])return new vi(function(){return a[Symbol.iterator]()});
if("function"==typeof a.da)return new vi(function(){return a.da()});
throw Error("Not an iterator or iterable.");}
function vi(a){this.i=a}
vi.prototype.da=function(){return new wi(this.i())};
vi.prototype[Symbol.iterator]=function(){return new xi(this.i())};
vi.prototype.h=function(){return new xi(this.i())};
function wi(a){this.i=a}
u(wi,ri);wi.prototype.next=function(){return this.i.next()};
wi.prototype[Symbol.iterator]=function(){return new xi(this.i)};
wi.prototype.h=function(){return new xi(this.i)};
function xi(a){vi.call(this,function(){return a});
this.j=a}
u(xi,vi);xi.prototype.next=function(){return this.j.next()};function yi(a,b){this.i={};this.h=[];this.qa=this.size=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof yi)for(c=a.xb(),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
k=yi.prototype;k.xb=function(){zi(this);return this.h.concat()};
k.has=function(a){return Ai(this.i,a)};
k.equals=function(a,b){if(this===a)return!0;if(this.size!=a.size)return!1;b=b||Bi;zi(this);for(var c,d=0;c=this.h[d];d++)if(!b(this.get(c),a.get(c)))return!1;return!0};
function Bi(a,b){return a===b}
k.Na=function(){return 0==this.size};
k.clear=function(){this.i={};this.qa=this.size=this.h.length=0};
k.remove=function(a){return this.delete(a)};
k.delete=function(a){return Ai(this.i,a)?(delete this.i[a],--this.size,this.qa++,this.h.length>2*this.size&&zi(this),!0):!1};
function zi(a){if(a.size!=a.h.length){for(var b=0,c=0;b<a.h.length;){var d=a.h[b];Ai(a.i,d)&&(a.h[c++]=d);b++}a.h.length=c}if(a.size!=a.h.length){var e={};for(c=b=0;b<a.h.length;)d=a.h[b],Ai(e,d)||(a.h[c++]=d,e[d]=1),b++;a.h.length=c}}
k.get=function(a,b){return Ai(this.i,a)?this.i[a]:b};
k.set=function(a,b){Ai(this.i,a)||(this.size+=1,this.h.push(a),this.qa++);this.i[a]=b};
k.forEach=function(a,b){for(var c=this.xb(),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
k.clone=function(){return new yi(this)};
k.keys=function(){return ui(this.da(!0)).h()};
k.values=function(){return ui(this.da(!1)).h()};
k.entries=function(){var a=this;return ji(this.keys(),function(b){return[b,a.get(b)]})};
k.da=function(a){zi(this);var b=0,c=this.qa,d=this,e=new ri;e.next=function(){if(c!=d.qa)throw Error("The map has changed since the iterator was created");if(b>=d.h.length)return si;var f=d.h[b++];return ti(a?f:d.i[f])};
return e};
function Ai(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
;function K(a){J.call(this);this.o=1;this.l=[];this.m=0;this.i=[];this.j={};this.s=!!a}
ab(K,J);k=K.prototype;k.subscribe=function(a,b,c){var d=this.j[a];d||(d=this.j[a]=[]);var e=this.o;this.i[e]=a;this.i[e+1]=b;this.i[e+2]=c;this.o=e+3;d.push(e);return e};
function Ci(a,b,c,d){if(b=a.j[b]){var e=a.i;(b=b.find(function(f){return e[f+1]==c&&e[f+2]==d}))&&a.Ga(b)}}
k.Ga=function(a){var b=this.i[a];if(b){var c=this.j[b];0!=this.m?(this.l.push(a),this.i[a+1]=function(){}):(c&&mb(c,a),delete this.i[a],delete this.i[a+1],delete this.i[a+2])}return!!b};
k.sa=function(a,b){var c=this.j[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.s)for(e=0;e<c.length;e++){var g=c[e];Di(this.i[g+1],this.i[g+2],d)}else{this.m++;try{for(e=0,f=c.length;e<f&&!this.h();e++)g=c[e],this.i[g+1].apply(this.i[g+2],d)}finally{if(this.m--,0<this.l.length&&0==this.m)for(;c=this.l.pop();)this.Ga(c)}}return 0!=e}return!1};
function Di(a,b,c){yf(function(){a.apply(b,c)})}
k.clear=function(a){if(a){var b=this.j[a];b&&(b.forEach(this.Ga,this),delete this.j[a])}else this.i.length=0,this.j={}};
k.B=function(){K.Y.B.call(this);this.clear();this.l.length=0};function Ei(a){this.h=a}
Ei.prototype.set=function(a,b){void 0===b?this.h.remove(a):this.h.set(a,Cg(b))};
Ei.prototype.get=function(a){try{var b=this.h.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Ei.prototype.remove=function(a){this.h.remove(a)};function Fi(a){this.h=a}
ab(Fi,Ei);function Gi(a){this.data=a}
function Hi(a){return void 0===a||a instanceof Gi?a:new Gi(a)}
Fi.prototype.set=function(a,b){Fi.Y.set.call(this,a,Hi(b))};
Fi.prototype.i=function(a){a=Fi.Y.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
Fi.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function Ii(a){this.h=a}
ab(Ii,Fi);Ii.prototype.set=function(a,b,c){if(b=Hi(b)){if(c){if(c<Date.now()){Ii.prototype.remove.call(this,a);return}b.expiration=c}b.creation=Date.now()}Ii.Y.set.call(this,a,b)};
Ii.prototype.i=function(a){var b=Ii.Y.i.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<Date.now()||c&&c>Date.now())Ii.prototype.remove.call(this,a);else return b}};function Ji(){}
;function Ki(){}
ab(Ki,Ji);Ki.prototype[Symbol.iterator]=function(){return ui(this.da(!0)).h()};
Ki.prototype.clear=function(){var a=Array.from(this);a=p(a);for(var b=a.next();!b.done;b=a.next())this.remove(b.value)};function Li(a){this.h=a}
ab(Li,Ki);k=Li.prototype;k.isAvailable=function(){if(!this.h)return!1;try{return this.h.setItem("__sak","1"),this.h.removeItem("__sak"),!0}catch(a){return!1}};
k.set=function(a,b){try{this.h.setItem(a,b)}catch(c){if(0==this.h.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
k.get=function(a){a=this.h.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.h.removeItem(a)};
k.da=function(a){var b=0,c=this.h,d=new ri;d.next=function(){if(b>=c.length)return si;var e=c.key(b++);if(a)return ti(e);e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return ti(e)};
return d};
k.clear=function(){this.h.clear()};
k.key=function(a){return this.h.key(a)};function Mi(){var a=null;try{a=window.localStorage||null}catch(b){}this.h=a}
ab(Mi,Li);function Ni(a,b){this.i=a;this.h=null;var c;if(c=Kc)c=!(9<=Number(Xc));if(c){Oi||(Oi=new yi);this.h=Oi.get(a);this.h||(b?this.h=document.getElementById(b):(this.h=document.createElement("userdata"),this.h.addBehavior("#default#userData"),document.body.appendChild(this.h)),Oi.set(a,this.h));try{this.h.load(this.i)}catch(d){this.h=null}}}
ab(Ni,Ki);var Pi={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},Oi=null;function Qi(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return Pi[b]})}
k=Ni.prototype;k.isAvailable=function(){return!!this.h};
k.set=function(a,b){this.h.setAttribute(Qi(a),b);Ri(this)};
k.get=function(a){a=this.h.getAttribute(Qi(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
k.remove=function(a){this.h.removeAttribute(Qi(a));Ri(this)};
k.da=function(a){var b=0,c=this.h.XMLDocument.documentElement.attributes,d=new ri;d.next=function(){if(b>=c.length)return si;var e=c[b++];if(a)return ti(decodeURIComponent(e.nodeName.replace(/\./g,"%")).slice(1));e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return ti(e)};
return d};
k.clear=function(){for(var a=this.h.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);Ri(this)};
function Ri(a){try{a.h.save(a.i)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function Si(a,b){this.i=a;this.h=b+"::"}
ab(Si,Ki);Si.prototype.set=function(a,b){this.i.set(this.h+a,b)};
Si.prototype.get=function(a){return this.i.get(this.h+a)};
Si.prototype.remove=function(a){this.i.remove(this.h+a)};
Si.prototype.da=function(a){var b=this.i[Symbol.iterator](),c=this,d=new ri;d.next=function(){var e=b.next();if(e.done)return e;for(e=e.value;e.slice(0,c.h.length)!=c.h;){e=b.next();if(e.done)return e;e=e.value}return ti(a?e.slice(c.h.length):c.i.get(e))};
return d};function Ti(a){this.name=a}
;var Ui=new Ti("rawColdConfigGroup");var Vi=new Ti("rawHotConfigGroup");function Wi(a){H.call(this,a)}
u(Wi,H);function Xi(a){H.call(this,a)}
u(Xi,H);Xi.prototype.getKey=function(){return Sd(this,1)};
Xi.prototype.getValue=function(){return ee(this,2===Xd(this,Yi)?2:-1)};
var Yi=[2,3,4,5,6];function Zi(a){H.call(this,a)}
u(Zi,H);function $i(a){H.call(this,a)}
u($i,H);function aj(a){H.call(this,a,-1,bj)}
u(aj,H);var bj=[2];function cj(a){H.call(this,a,-1,dj)}
u(cj,H);cj.prototype.getPlayerType=function(){return Sd(this,36)};
cj.prototype.setHomeGroupInfo=function(a){return G(this,aj,81,a)};
cj.prototype.clearLocationPlayabilityToken=function(){return D(this,89,void 0,!1)};
var dj=[9,66,24,32,86,100,101];function ej(a){H.call(this,a,-1,fj)}
u(ej,H);var fj=[15,26,28];function gj(a){H.call(this,a,-1,hj)}
u(gj,H);var hj=[5];function ij(a){H.call(this,a)}
u(ij,H);function jj(a){H.call(this,a,-1,kj)}
u(jj,H);jj.prototype.setSafetyMode=function(a){return D(this,5,a)};
var kj=[12];function lj(a){H.call(this,a,-1,mj)}
u(lj,H);lj.prototype.i=function(a){return G(this,cj,1,a)};
var mj=[12];var nj=new Ti("continuationCommand");var oj=new Ti("webCommandMetadata");var pj=new Ti("signalServiceEndpoint");var qj={wi:"EMBEDDED_PLAYER_MODE_UNKNOWN",si:"EMBEDDED_PLAYER_MODE_DEFAULT",vi:"EMBEDDED_PLAYER_MODE_PFP",ti:"EMBEDDED_PLAYER_MODE_PFL"};var rj=new Ti("feedbackEndpoint");var sj={Vq:"WEB_DISPLAY_MODE_UNKNOWN",Rq:"WEB_DISPLAY_MODE_BROWSER",Tq:"WEB_DISPLAY_MODE_MINIMAL_UI",Uq:"WEB_DISPLAY_MODE_STANDALONE",Sq:"WEB_DISPLAY_MODE_FULLSCREEN"};function tj(a){H.call(this,a,-1,uj)}
u(tj,H);function vj(a){H.call(this,a)}
u(vj,H);vj.prototype.getKey=function(){return fe(Sd(this,1),"")};
vj.prototype.getValue=function(){return fe(Sd(this,2),"")};
var uj=[4,5];function wj(a){H.call(this,a)}
u(wj,H);function xj(a){H.call(this,a)}
u(xj,H);var yj=[2,3,4];function zj(a){H.call(this,a)}
u(zj,H);zj.prototype.getMessage=function(){return fe(Sd(this,1),"")};function Aj(a){H.call(this,a)}
u(Aj,H);function Bj(a){H.call(this,a)}
u(Bj,H);function Cj(a){H.call(this,a,-1,Dj)}
u(Cj,H);var Dj=[10,17];function Ej(a){H.call(this,a)}
u(Ej,H);function Fj(a){H.call(this,a)}
u(Fj,H);function Gj(a){H.call(this,a)}
u(Gj,H);function Hj(a){H.call(this,a)}
u(Hj,H);function Ij(a){H.call(this,a)}
u(Ij,H);function Jj(a){H.call(this,a,-1,Kj)}
u(Jj,H);Jj.prototype.getVideoData=function(){return Yd(this,Ij,15)};
var Kj=[4];function Lj(a){H.call(this,a)}
u(Lj,H);function Mj(a,b){return G(a,Gj,1,b)}
Lj.prototype.i=function(a){return D(this,2,a)};
function Nj(a){H.call(this,a)}
u(Nj,H);function Oj(a,b){G(a,Gj,1,b)}
;function Pj(a){H.call(this,a,-1,Qj)}
u(Pj,H);Pj.prototype.i=function(a){return D(this,1,a)};
function Rj(a,b){return G(a,Gj,2,b)}
var Qj=[3];function Sj(a){H.call(this,a)}
u(Sj,H);Sj.prototype.i=function(a){return D(this,1,a)};function Tj(a){H.call(this,a)}
u(Tj,H);Tj.prototype.i=function(a){return D(this,1,a)};function Uj(a){H.call(this,a)}
u(Uj,H);Uj.prototype.i=function(a){return D(this,1,a)};function Vj(a){H.call(this,a)}
u(Vj,H);Vj.prototype.i=function(a){return D(this,1,a)};function Wj(a){H.call(this,a)}
u(Wj,H);function Xj(a){H.call(this,a)}
u(Xj,H);function Yj(a){H.call(this,a,-1,Zj)}
u(Yj,H);Yj.prototype.getPlayerType=function(){var a=Sd(this,7);return null==a?0:a};
Yj.prototype.setVideoId=function(a){return D(this,19,a)};
function ak(a,b){de(a,68,bk,b)}
function bk(a){H.call(this,a)}
u(bk,H);bk.prototype.getId=function(){return fe(Sd(this,2),"")};
var Zj=[83,68];function ck(a){H.call(this,a)}
u(ck,H);function dk(a){H.call(this,a)}
u(dk,H);function ek(a){H.call(this,a)}
u(ek,H);function fk(a){H.call(this,a,459)}
u(fk,H);
var gk=[23,24,11,6,7,5,2,3,13,20,21,22,28,32,37,229,241,45,59,225,288,72,73,78,208,156,202,215,74,76,79,80,111,85,91,97,100,102,105,119,126,127,136,146,148,151,157,158,159,163,164,168,444,176,222,383,177,178,179,458,411,184,188,189,190,191,193,194,195,196,197,198,199,200,201,402,320,203,204,205,206,258,259,260,261,327,209,219,226,227,232,233,234,240,244,247,248,249,251,256,257,266,254,255,270,272,278,291,293,300,304,308,309,310,311,313,314,319,321,323,324,328,330,331,332,334,337,338,340,344,348,350,
351,352,353,354,355,356,357,358,361,363,364,368,369,370,373,374,375,378,380,381,388,389,403,410,412,429,413,414,415,416,417,418,430,423,424,425,426,427,431,117,439,441,448];var hk={vj:0,gj:1,mj:2,nj:4,sj:8,oj:16,pj:32,uj:64,tj:128,ij:256,kj:512,rj:1024,jj:2048,lj:4096,hj:8192,qj:16384};function ik(a){H.call(this,a)}
u(ik,H);function jk(a){H.call(this,a)}
u(jk,H);jk.prototype.setVideoId=function(a){return Wd(this,1,Ek,a)};
jk.prototype.getPlaylistId=function(){return ee(this,2===Xd(this,Ek)?2:-1)};
var Ek=[1,2];function Fk(a){H.call(this,a,-1,Gk)}
u(Fk,H);var Gk=[3];var Hk=new Ti("webPlayerShareEntityServiceEndpoint");var Ik=new Ti("playlistEditEndpoint");var Jk=new Ti("modifyChannelNotificationPreferenceEndpoint");var Kk=new Ti("unsubscribeEndpoint");var Lk=new Ti("subscribeEndpoint");function Mk(a,b){1<b.length?a[b[0]]=b[1]:1===b.length&&Object.assign(a,b[0])}
;var Nk=y.window,Ok,Pk,Qk=(null==Nk?void 0:null==(Ok=Nk.yt)?void 0:Ok.config_)||(null==Nk?void 0:null==(Pk=Nk.ytcfg)?void 0:Pk.data_)||{};z("yt.config_",Qk);function Rk(){Mk(Qk,arguments)}
function L(a,b){return a in Qk?Qk[a]:b}
function Sk(){var a=Qk.EXPERIMENT_FLAGS;return a?a.web_disable_gel_stp_ecatcher_killswitch:void 0}
;function M(a){a=Tk(a);return"string"===typeof a&&"false"===a?!1:!!a}
function Uk(a,b){a=Tk(a);return void 0===a&&void 0!==b?b:Number(a||0)}
function Vk(){return L("EXPERIMENTS_TOKEN","")}
function Tk(a){var b=L("EXPERIMENTS_FORCED_FLAGS",{})||{};return void 0!==b[a]?b[a]:L("EXPERIMENT_FLAGS",{})[a]}
function Wk(){for(var a=[],b=L("EXPERIMENTS_FORCED_FLAGS",{}),c=p(Object.keys(b)),d=c.next();!d.done;d=c.next())d=d.value,a.push({key:d,value:String(b[d])});c=L("EXPERIMENT_FLAGS",{});var e=p(Object.keys(c));for(d=e.next();!d.done;d=e.next())d=d.value,d.startsWith("force_")&&void 0===b[d]&&a.push({key:d,value:String(c[d])});return a}
;function Xk(){var a=Yk;B("yt.ads.biscotti.getId_")||z("yt.ads.biscotti.getId_",a)}
function Zk(a){z("yt.ads.biscotti.lastId_",a)}
;var $k=[];function al(a){$k.forEach(function(b){return b(a)})}
function bl(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){cl(b)}}:a}
function cl(a,b,c,d){var e=B("yt.logging.errors.log");e?e(a,"ERROR",b,c,d):(e=L("ERRORS",[]),e.push([a,"ERROR",b,c,d]),Rk("ERRORS",e));al(a)}
function dl(a,b,c,d){var e=B("yt.logging.errors.log");e?e(a,"WARNING",b,c,d):(e=L("ERRORS",[]),e.push([a,"WARNING",b,c,d]),Rk("ERRORS",e))}
;var el=/^[\w.]*$/,fl={q:!0,search_query:!0};function gl(a,b){b=a.split(b);for(var c={},d=0,e=b.length;d<e;d++){var f=b[d].split("=");if(1==f.length&&f[0]||2==f.length)try{var g=hl(f[0]||""),h=hl(f[1]||"");g in c?Array.isArray(c[g])?nb(c[g],h):c[g]=[c[g],h]:c[g]=h}catch(r){var l=r,m=f[0],q=String(gl);l.args=[{key:m,value:f[1],query:a,method:il==q?"unchanged":q}];fl.hasOwnProperty(m)||dl(l)}}return c}
var il=String(gl);function jl(a){var b=[];ob(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];hb(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function kl(a){"?"==a.charAt(0)&&(a=a.substr(1));return gl(a,"&")}
function ll(a){return-1!=a.indexOf("?")?(a=(a||"").split("#")[0],a=a.split("?",2),kl(1<a.length?a[1]:a[0])):{}}
function ml(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=kl(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);return wc(a,e)+d}
function nl(a){if(!b)var b=window.location.href;var c=oc(1,a),d=pc(a);c&&d?(a=a.match(mc),b=b.match(mc),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?pc(b)==d&&(Number(oc(4,b))||null)==(Number(oc(4,a))||null):!0;return a}
function hl(a){return a&&a.match(el)?a:decodeURIComponent(a.replace(/\+/g," "))}
;function ol(a){var b=pl;a=void 0===a?B("yt.ads.biscotti.lastId_")||"":a;var c=Object,d=c.assign,e={};e.dt=$h;e.flash="0";a:{try{var f=b.h.top.location.href}catch(ea){f=2;break a}f=f?f===b.i.location.href?0:1:2}e=(e.frm=f,e);try{e.u_tz=-(new Date).getTimezoneOffset();var g=void 0===g?Hh:g;try{var h=g.history.length}catch(ea){h=0}e.u_his=h;var l;e.u_h=null==(l=Hh.screen)?void 0:l.height;var m;e.u_w=null==(m=Hh.screen)?void 0:m.width;var q;e.u_ah=null==(q=Hh.screen)?void 0:q.availHeight;var r;e.u_aw=
null==(r=Hh.screen)?void 0:r.availWidth;var w;e.u_cd=null==(w=Hh.screen)?void 0:w.colorDepth}catch(ea){}h=b.h;try{var t=h.screenX;var A=h.screenY}catch(ea){}try{var E=h.outerWidth;var F=h.outerHeight}catch(ea){}try{var O=h.innerWidth;var N=h.innerHeight}catch(ea){}try{var R=h.screenLeft;var ca=h.screenTop}catch(ea){}try{O=h.innerWidth,N=h.innerHeight}catch(ea){}try{var U=h.screen.availWidth;var rb=h.screen.availTop}catch(ea){}t=[R,ca,t,A,U,rb,E,F,O,N];try{var Wa=(b.h.top||window).document,oa="CSS1Compat"==
Wa.compatMode?Wa.documentElement:Wa.body;var I=(new mf(oa.clientWidth,oa.clientHeight)).round()}catch(ea){I=new mf(-12245933,-12245933)}Wa=I;I={};var ma=void 0===ma?y:ma;oa=new gi;ma.SVGElement&&ma.document.createElementNS&&oa.set(0);A=Xh();A["allow-top-navigation-by-user-activation"]&&oa.set(1);A["allow-popups-to-escape-sandbox"]&&oa.set(2);ma.crypto&&ma.crypto.subtle&&oa.set(3);ma.TextDecoder&&ma.TextEncoder&&oa.set(4);ma=hi(oa);I.bc=ma;I.bih=Wa.height;I.biw=Wa.width;I.brdim=t.join();b=b.i;b=(I.vis=
b.prerendering?3:{visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]||0,I.wgl=!!Hh.WebGLRenderingContext,I);c=d.call(c,e,b);c.ca_type="image";a&&(c.bid=a);return c}
var pl=new function(){var a=window.document;this.h=window;this.i=a};
z("yt.ads_.signals_.getAdSignalsString",function(a){return jl(ol(a))});Date.now();var ql="XMLHttpRequest"in y?function(){return new XMLHttpRequest}:null;
function rl(){if(!ql)return null;var a=ql();return"open"in a?a:null}
function sl(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function tl(a,b){"function"===typeof a&&(a=bl(a));return window.setTimeout(a,b)}
;var ul={Authorization:"AUTHORIZATION","X-Goog-EOM-Visitor-Id":"EOM_VISITOR_DATA","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL",
"X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},vl="app debugcss debugjs expflag force_ad_params force_ad_encrypted force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" ").concat(ja(ai)),wl=!1;
function xl(a,b){b=void 0===b?{}:b;var c=nl(a),d=M("web_ajax_ignore_global_headers_if_set"),e;for(e in ul){var f=L(ul[e]);"X-Goog-Visitor-Id"!==e||f||(f=L("VISITOR_DATA"));!f||!c&&pc(a)||d&&void 0!==b[e]||(b[e]=f)}"X-Goog-EOM-Visitor-Id"in b&&"X-Goog-Visitor-Id"in b&&delete b["X-Goog-Visitor-Id"];if(c||!pc(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!pc(a)){try{var g=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch(h){}g&&(b["X-YouTube-Time-Zone"]=g)}document.location.hostname.endsWith("youtubeeducation.com")||
!c&&pc(a)||(b["X-YouTube-Ad-Signals"]=jl(ol()));return b}
function yl(a){var b=window.location.search,c=pc(a);M("debug_handle_relative_url_for_query_forward_killswitch")||!c&&nl(a)&&(c=document.location.hostname);var d=nc(oc(5,a));d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=kl(b),f={};hb(vl,function(g){e[g]&&(f[g]=e[g])});
return ml(a,f||{},!1)}
function zl(a,b){var c=b.format||"JSON";a=Al(a,b);var d=Bl(a,b),e=!1,f=Cl(a,function(l){if(!e){e=!0;h&&window.clearTimeout(h);var m=sl(l),q=null,r=400<=l.status&&500>l.status,w=500<=l.status&&600>l.status;if(m||r||w)q=Dl(a,c,l,b.convertToSafeHtml);if(m)a:if(l&&204==l.status)m=!0;else{switch(c){case "XML":m=0==parseInt(q&&q.return_code,10);break a;case "RAW":m=!0;break a}m=!!q}q=q||{};r=b.context||y;m?b.onSuccess&&b.onSuccess.call(r,l,q):b.onError&&b.onError.call(r,l,q);b.onFinish&&b.onFinish.call(r,
l,q)}},b.method,d,b.headers,b.responseType,b.withCredentials);
d=b.timeout||0;if(b.onTimeout&&0<d){var g=b.onTimeout;var h=tl(function(){e||(e=!0,f.abort(),window.clearTimeout(h),g.call(b.context||y,f))},d)}return f}
function Al(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=L("XSRF_FIELD_NAME");if(b=b.urlParams)b[c]&&delete b[c],a=ml(a,b||{},!0);return a}
function Bl(a,b){var c=L("XSRF_FIELD_NAME"),d=L("XSRF_TOKEN"),e=b.postBody||"",f=b.postParams,g=L("XSRF_FIELD_NAME"),h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||pc(a)&&!b.withCredentials&&pc(a)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);(M("ajax_parse_query_data_only_when_filled")&&f&&0<Object.keys(f).length||f)&&"string"===typeof e&&(e=kl(e),zb(e,f),e=b.postBodyFormat&&"JSON"==b.postBodyFormat?
JSON.stringify(e):uc(e));f=e||f&&!sb(f);!wl&&f&&"POST"!=b.method&&(wl=!0,cl(Error("AJAX request with postData should use POST")));return e}
function Dl(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,dl(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(")]}'\n"===f.substring(0,5)&&(f=f.substring(5)),e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?El(a):null)e={},hb(a.getElementsByTagName("*"),function(g){e[g.tagName]=Fl(g)})}d&&Gl(e);
return e}
function Gl(a){if(Sa(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;Eb("HTML that is escaped and sanitized server-side and passed through yt.net.ajax");var d=a[b],e=Bb();d=e?e.createHTML(d):d;a[c]=new fc(d)}else Gl(a[b])}}
function El(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Fl(a){var b="";hb(a.childNodes,function(c){b+=c.nodeValue});
return b}
function Cl(a,b,c,d,e,f,g){function h(){4==(l&&"readyState"in l?l.readyState:0)&&b&&bl(b)(l)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var l=rl();if(!l)return null;"onloadend"in l?l.addEventListener("loadend",h,!1):l.onreadystatechange=h;M("debug_forward_web_query_parameters")&&(a=yl(a));l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=xl(a,e))for(var m in e)l.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");l.send(d);
return l}
;var Hl=Yc||Zc;function Il(a){var b=Ub();return b?0<=b.toLowerCase().indexOf(a):!1}
;var Jl=[{Cb:function(a){return"Cannot read property '"+a.key+"'"},
kb:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{Cb:function(a){return"Cannot call '"+a.key+"'"},
kb:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{Cb:function(a){return a.key+" is not defined"},
kb:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var Ll={na:[],la:[{callback:Kl,weight:500}]};function Kl(a){if("JavaException"===a.name)return!0;a=a.stack;return a.includes("chrome://")||a.includes("chrome-extension://")||a.includes("moz-extension://")}
;function Ml(){this.la=[];this.na=[]}
var Nl;function Ol(){if(!Nl){var a=Nl=new Ml;a.na.length=0;a.la.length=0;Ll.na&&a.na.push.apply(a.na,Ll.na);Ll.la&&a.la.push.apply(a.la,Ll.la)}return Nl}
;var Pl=new K;function Ql(a){function b(){return a.charCodeAt(d++)}
var c=a.length,d=0;do{var e=Rl(b);if(Infinity===e)break;var f=e>>3;switch(e&7){case 0:e=Rl(b);if(2===f)return e;break;case 1:if(2===f)return;d+=8;break;case 2:e=Rl(b);if(2===f)return a.substr(d,e);d+=e;break;case 5:if(2===f)return;d+=4;break;default:return}}while(d<c)}
function Rl(a){var b=a(),c=b&127;if(128>b)return c;b=a();c|=(b&127)<<7;if(128>b)return c;b=a();c|=(b&127)<<14;if(128>b)return c;b=a();return 128>b?c|(b&127)<<21:Infinity}
;function Sl(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Tl(d,a[d],b,c),500<e));d++);d=e}else if("object"===typeof a)for(e in a){if(a[e]){var f=a[e];var g=b;var h=c;g="string"!==typeof f||"clickTrackingParams"!==e&&"trackingParams"!==e?0:(f=Ql(atob(f.replace(/-/g,"+").replace(/_/g,"/"))))?Tl(e+".ve",f,g,h):0;d+=g;d+=Tl(e,a[e],b,c);if(500<d)break}}else c[b]=Ul(a),d+=c[b].length;else c[b]=Ul(a),d+=c[b].length;return d}
function Tl(a,b,c,d){c+="."+a;a=Ul(b);d[c]=a;return c.length+a.length}
function Ul(a){try{return("string"===typeof a?a:String(JSON.stringify(a))).substr(0,500)}catch(b){return"unable to serialize "+typeof a+" ("+b.message+")"}}
;function Vl(a){var b=this;this.i=void 0;this.h=!1;a.addEventListener("beforeinstallprompt",function(c){c.preventDefault();b.i=c});
a.addEventListener("appinstalled",function(){b.h=!0},{once:!0})}
function Wl(){if(!y.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return y.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":y.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":y.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":y.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
;function Xl(a,b,c,d,e){ug.set(""+a,b,{ib:c,path:"/",domain:void 0===d?"youtube.com":d,secure:void 0===e?!1:e})}
function Yl(a,b,c){ug.remove(""+a,void 0===b?"/":b,void 0===c?"youtube.com":c)}
function Zl(){if(!ug.isEnabled())return!1;if(!ug.Na())return!0;ug.set("TESTCOOKIESENABLED","1",{ib:60});if("1"!==ug.get("TESTCOOKIESENABLED"))return!1;ug.remove("TESTCOOKIESENABLED");return!0}
;var $l=B("ytglobal.prefsUserPrefsPrefs_")||{};z("ytglobal.prefsUserPrefsPrefs_",$l);function am(){this.h=L("ALT_PREF_COOKIE_NAME","PREF");this.i=L("ALT_PREF_COOKIE_DOMAIN","youtube.com");var a=ug.get(""+this.h,void 0);if(a){a=decodeURIComponent(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&($l[d]=c.toString())}}}
am.prototype.get=function(a,b){bm(a);cm(a);a=void 0!==$l[a]?$l[a].toString():null;return null!=a?a:b?b:""};
am.prototype.set=function(a,b){bm(a);cm(a);if(null==b)throw Error("ExpectedNotNull");$l[a]=b.toString()};
function dm(a){return!!((em("f"+(Math.floor(a/31)+1))||0)&1<<a%31)}
am.prototype.remove=function(a){bm(a);cm(a);delete $l[a]};
am.prototype.clear=function(){for(var a in $l)delete $l[a]};
function cm(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function bm(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function em(a){a=void 0!==$l[a]?$l[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
Pa(am);var fm={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},gm={CONN_DEFAULT:0,CONN_UNKNOWN:1,CONN_NONE:2,CONN_WIFI:3,CONN_CELLULAR_2G:4,CONN_CELLULAR_3G:5,CONN_CELLULAR_4G:6,CONN_CELLULAR_UNKNOWN:7,CONN_DISCO:8,CONN_CELLULAR_5G:9,CONN_WIFI_METERED:10,CONN_CELLULAR_5G_SA:11,
CONN_CELLULAR_5G_NSA:12,CONN_INVALID:31},hm={EFFECTIVE_CONNECTION_TYPE_UNKNOWN:0,EFFECTIVE_CONNECTION_TYPE_OFFLINE:1,EFFECTIVE_CONNECTION_TYPE_SLOW_2G:2,EFFECTIVE_CONNECTION_TYPE_2G:3,EFFECTIVE_CONNECTION_TYPE_3G:4,EFFECTIVE_CONNECTION_TYPE_4G:5},im={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};function jm(){var a=y.navigator;return a?a.connection:void 0}
function km(){var a=jm();if(a){var b=fm[a.type||"unknown"]||"CONN_UNKNOWN";a=fm[a.effectiveType||"unknown"]||"CONN_UNKNOWN";"CONN_CELLULAR_UNKNOWN"===b&&"CONN_UNKNOWN"!==a&&(b=a);if("CONN_UNKNOWN"!==b)return b;if("CONN_UNKNOWN"!==a)return a}}
function lm(){var a=jm();if(null!=a&&a.effectiveType)return im.hasOwnProperty(a.effectiveType)?im[a.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN"}
;function mm(){}
function nm(a,b){return om(a,0,b)}
mm.prototype.S=function(a,b){return om(a,1,b)};
function pm(a,b){om(a,2,b)}
function qm(a){var b=B("yt.scheduler.instance.addImmediateJob");b?b(a):a()}
;function rm(){mm.apply(this,arguments)}
u(rm,mm);function sm(){rm.h||(rm.h=new rm);return rm.h}
function om(a,b,c){void 0!==c&&Number.isNaN(Number(c))&&(c=void 0);var d=B("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):tl(a,c||0)}
rm.prototype.ea=function(a){if(void 0===a||!Number.isNaN(Number(a))){var b=B("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}};
rm.prototype.start=function(){var a=B("yt.scheduler.instance.start");a&&a()};
rm.prototype.pause=function(){var a=B("yt.scheduler.instance.pause");a&&a()};
var fi=sm();function P(a){var b=Ka.apply(1,arguments);var c=Error.call(this,a);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.args=[].concat(ja(b))}
u(P,Error);function tm(){try{return um(),!0}catch(a){return!1}}
function um(a){if(void 0!==L("DATASYNC_ID"))return L("DATASYNC_ID");throw new P("Datasync ID not set",void 0===a?"unknown":a);}
;function vm(a){var b=new Mi;(b=b.isAvailable()?a?new Si(b,a):b:null)||(a=new Ni(a||"UserDataSharedStore"),b=a.isAvailable()?a:null);this.h=(a=b)?new Ii(a):null;this.i=document.domain||window.location.hostname}
vm.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.h)try{this.h.set(a,b,Date.now()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Cg(b))}catch(f){return}else e=escape(b);Xl(a,e,c,this.i)};
vm.prototype.get=function(a,b){var c=void 0,d=!this.h;if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=ug.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
vm.prototype.remove=function(a){this.h&&this.h.remove(a);Yl(a,"/",this.i)};var wm=function(){var a;return function(){a||(a=new vm("ytidb"));return a}}();
function xm(){var a;return null==(a=wm())?void 0:a.get("LAST_RESULT_ENTRY_KEY",!0)}
;var ym=[],zm,Am=!1;function Bm(){var a={};for(zm=new Cm(void 0===a.handleError?Dm:a.handleError,void 0===a.logEvent?Em:a.logEvent);0<ym.length;)switch(a=ym.shift(),a.type){case "ERROR":zm.handleError(a.payload);break;case "EVENT":zm.logEvent(a.eventType,a.payload)}}
function Fm(a){Am||(zm?zm.handleError(a):(ym.push({type:"ERROR",payload:a}),10<ym.length&&ym.shift()))}
function Gm(a,b){Am||(zm?zm.logEvent(a,b):(ym.push({type:"EVENT",eventType:a,payload:b}),10<ym.length&&ym.shift()))}
;function Hm(a){if(0<=a.indexOf(":"))throw Error("Database name cannot contain ':'");}
function Im(a){return a.substr(0,a.indexOf(":"))||a}
;var Jm={},Km=(Jm.AUTH_INVALID="No user identifier specified.",Jm.EXPLICIT_ABORT="Transaction was explicitly aborted.",Jm.IDB_NOT_SUPPORTED="IndexedDB is not supported.",Jm.MISSING_INDEX="Index not created.",Jm.MISSING_OBJECT_STORES="Object stores not created.",Jm.DB_DELETED_BY_MISSING_OBJECT_STORES="Database is deleted because expected object stores were not created.",Jm.DB_REOPENED_BY_MISSING_OBJECT_STORES="Database is reopened because expected object stores were not created.",Jm.UNKNOWN_ABORT="Transaction was aborted for unknown reasons.",
Jm.QUOTA_EXCEEDED="The current transaction exceeded its quota limitations.",Jm.QUOTA_MAYBE_EXCEEDED="The current transaction may have failed because of exceeding quota limitations.",Jm.EXECUTE_TRANSACTION_ON_CLOSED_DB="Can't start a transaction on a closed database",Jm.INCOMPATIBLE_DB_VERSION="The binary is incompatible with the database version",Jm),Lm={},Mm=(Lm.AUTH_INVALID="ERROR",Lm.EXECUTE_TRANSACTION_ON_CLOSED_DB="WARNING",Lm.EXPLICIT_ABORT="IGNORED",Lm.IDB_NOT_SUPPORTED="ERROR",Lm.MISSING_INDEX=
"WARNING",Lm.MISSING_OBJECT_STORES="ERROR",Lm.DB_DELETED_BY_MISSING_OBJECT_STORES="WARNING",Lm.DB_REOPENED_BY_MISSING_OBJECT_STORES="WARNING",Lm.QUOTA_EXCEEDED="WARNING",Lm.QUOTA_MAYBE_EXCEEDED="WARNING",Lm.UNKNOWN_ABORT="WARNING",Lm.INCOMPATIBLE_DB_VERSION="WARNING",Lm),Nm={},Om=(Nm.AUTH_INVALID=!1,Nm.EXECUTE_TRANSACTION_ON_CLOSED_DB=!1,Nm.EXPLICIT_ABORT=!1,Nm.IDB_NOT_SUPPORTED=!1,Nm.MISSING_INDEX=!1,Nm.MISSING_OBJECT_STORES=!1,Nm.DB_DELETED_BY_MISSING_OBJECT_STORES=!1,Nm.DB_REOPENED_BY_MISSING_OBJECT_STORES=
!1,Nm.QUOTA_EXCEEDED=!1,Nm.QUOTA_MAYBE_EXCEEDED=!0,Nm.UNKNOWN_ABORT=!0,Nm.INCOMPATIBLE_DB_VERSION=!1,Nm);function Pm(a,b,c,d,e){b=void 0===b?{}:b;c=void 0===c?Km[a]:c;d=void 0===d?Mm[a]:d;e=void 0===e?Om[a]:e;P.call(this,c,Object.assign({},{name:"YtIdbKnownError",isSw:void 0===self.document,isIframe:self!==self.top,type:a},b));this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,Pm.prototype)}
u(Pm,P);function Qm(a,b){Pm.call(this,"MISSING_OBJECT_STORES",{expectedObjectStores:b,foundObjectStores:a},Km.MISSING_OBJECT_STORES);Object.setPrototypeOf(this,Qm.prototype)}
u(Qm,Pm);function Rm(a,b){var c=Error.call(this);this.message=c.message;"stack"in c&&(this.stack=c.stack);this.index=a;this.objectStore=b;Object.setPrototypeOf(this,Rm.prototype)}
u(Rm,Error);var Sm=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function Tm(a,b,c,d){b=Im(b);var e=a instanceof Error?a:Error("Unexpected error: "+a);if(e instanceof Pm)return e;a={objectStoreNames:c,dbName:b,dbVersion:d};if("QuotaExceededError"===e.name)return new Pm("QUOTA_EXCEEDED",a);if($c&&"UnknownError"===e.name)return new Pm("QUOTA_MAYBE_EXCEEDED",a);if(e instanceof Rm)return new Pm("MISSING_INDEX",Object.assign({},a,{objectStore:e.objectStore,index:e.index}));if("InvalidStateError"===e.name&&Sm.some(function(f){return e.message.includes(f)}))return new Pm("EXECUTE_TRANSACTION_ON_CLOSED_DB",
a);
if("AbortError"===e.name)return new Pm("UNKNOWN_ABORT",a,e.message);e.args=[Object.assign({},a,{name:"IdbError",jc:e.name})];e.level="WARNING";return e}
function Um(a,b,c){var d=xm();return new Pm("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c,hasSucceededOnce:null==d?void 0:d.hasSucceededOnce}})}
;function Vm(a){if(!a)throw Error();throw a;}
function Wm(a){return a}
function Xm(a){this.h=a}
function Ym(a){function b(e){if("PENDING"===d.state.status){d.state={status:"REJECTED",reason:e};e=p(d.i);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
function c(e){if("PENDING"===d.state.status){d.state={status:"FULFILLED",value:e};e=p(d.h);for(var f=e.next();!f.done;f=e.next())f=f.value,f()}}
var d=this;this.state={status:"PENDING"};this.h=[];this.i=[];a=a.h;try{a(c,b)}catch(e){b(e)}}
Ym.all=function(a){return new Ym(new Xm(function(b,c){var d=[],e=a.length;0===e&&b(d);for(var f={za:0};f.za<a.length;f={za:f.za},++f.za)Ym.resolve(a[f.za]).then(function(g){return function(h){d[g.za]=h;e--;0===e&&b(d)}}(f)).catch(function(g){c(g)})}))};
Ym.resolve=function(a){return new Ym(new Xm(function(b,c){a instanceof Ym?a.then(b,c):b(a)}))};
Ym.reject=function(a){return new Ym(new Xm(function(b,c){c(a)}))};
Ym.prototype.then=function(a,b){var c=this,d=null!=a?a:Wm,e=null!=b?b:Vm;return new Ym(new Xm(function(f,g){"PENDING"===c.state.status?(c.h.push(function(){Zm(c,c,d,f,g)}),c.i.push(function(){$m(c,c,e,f,g)})):"FULFILLED"===c.state.status?Zm(c,c,d,f,g):"REJECTED"===c.state.status&&$m(c,c,e,f,g)}))};
Ym.prototype.catch=function(a){return this.then(void 0,a)};
function Zm(a,b,c,d,e){try{if("FULFILLED"!==a.state.status)throw Error("calling handleResolve before the promise is fulfilled.");var f=c(a.state.value);f instanceof Ym?an(a,b,f,d,e):d(f)}catch(g){e(g)}}
function $m(a,b,c,d,e){try{if("REJECTED"!==a.state.status)throw Error("calling handleReject before the promise is rejected.");var f=c(a.state.reason);f instanceof Ym?an(a,b,f,d,e):d(f)}catch(g){e(g)}}
function an(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(function(f){f instanceof Ym?an(a,b,f,d,e):d(f)},function(f){e(f)})}
;function bn(a,b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){try{a.removeEventListener("success",e),a.removeEventListener("error",d)}catch(g){}}
a.addEventListener("success",e);a.addEventListener("error",d)}
function cn(a){return new Promise(function(b,c){bn(a,b,c)})}
function dn(a){return new Ym(new Xm(function(b,c){bn(a,b,c)}))}
;function en(a,b){return new Ym(new Xm(function(c,d){function e(){var f=a?b(a):null;f?f.then(function(g){a=g;e()},d):c()}
e()}))}
;var fn=window,Q=fn.ytcsi&&fn.ytcsi.now?fn.ytcsi.now:fn.performance&&fn.performance.timing&&fn.performance.now&&fn.performance.timing.navigationStart?function(){return fn.performance.timing.navigationStart+fn.performance.now()}:function(){return(new Date).getTime()};function gn(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(Q());this.i=!1}
k=gn.prototype;k.add=function(a,b,c){return hn(this,[a],{mode:"readwrite",R:!0},function(d){return d.objectStore(a).add(b,c)})};
k.clear=function(a){return hn(this,[a],{mode:"readwrite",R:!0},function(b){return b.objectStore(a).clear()})};
k.close=function(){this.h.close();var a;(null==(a=this.options)?0:a.closed)&&this.options.closed()};
k.count=function(a,b){return hn(this,[a],{mode:"readonly",R:!0},function(c){return c.objectStore(a).count(b)})};
function jn(a,b,c){a=a.h.createObjectStore(b,c);return new kn(a)}
k.delete=function(a,b){return hn(this,[a],{mode:"readwrite",R:!0},function(c){return c.objectStore(a).delete(b)})};
k.get=function(a,b){return hn(this,[a],{mode:"readonly",R:!0},function(c){return c.objectStore(a).get(b)})};
function ln(a,b,c){return hn(a,[b],{mode:"readwrite",R:!0},function(d){d=d.objectStore(b);return dn(d.h.put(c,void 0))})}
k.objectStoreNames=function(){return Array.from(this.h.objectStoreNames)};
function hn(a,b,c,d){var e,f,g,h,l,m,q,r,w,t,A,E;return x(function(F){switch(F.h){case 1:var O={mode:"readonly",R:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};"string"===typeof c?O.mode=c:Object.assign(O,c);e=O;a.transactionCount++;f=e.R?3:1;g=0;case 2:if(h){F.u(3);break}g++;l=Math.round(Q());za(F,4);m=a.h.transaction(b,e.mode);O=new mn(m);O=nn(O,d);return v(F,O,6);case 6:return q=F.i,r=Math.round(Q()),on(a,l,r,g,void 0,b.join(),e),F.return(q);case 4:w=Ba(F);t=Math.round(Q());A=Tm(w,a.h.name,b.join(),a.h.version);
if((E=A instanceof Pm&&!A.h)||g>=f)on(a,l,t,g,A,b.join(),e),h=A;F.u(2);break;case 3:return F.return(Promise.reject(h))}})}
function on(a,b,c,d,e,f,g){b=c-b;e?(e instanceof Pm&&("QUOTA_EXCEEDED"===e.type||"QUOTA_MAYBE_EXCEEDED"===e.type)&&Gm("QUOTA_EXCEEDED",{dbName:Im(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof Pm&&"UNKNOWN_ABORT"===e.type&&(c-=a.j,0>c&&c>=Math.pow(2,31)&&(c=0),Gm("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),pn(a,!1,d,f,b,g.tag),Fm(e)):pn(a,!0,d,f,b,g.tag)}
function pn(a,b,c,d,e,f){Gm("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:void 0===f?"IDB_TRANSACTION_TAG_UNKNOWN":f})}
k.getName=function(){return this.h.name};
function kn(a){this.h=a}
k=kn.prototype;k.add=function(a,b){return dn(this.h.add(a,b))};
k.autoIncrement=function(){return this.h.autoIncrement};
k.clear=function(){return dn(this.h.clear()).then(function(){})};
function qn(a,b,c){a.h.createIndex(b,c,{unique:!1})}
k.count=function(a){return dn(this.h.count(a))};
function rn(a,b){return sn(a,{query:b},function(c){return c.delete().then(function(){return c.continue()})}).then(function(){})}
k.delete=function(a){return a instanceof IDBKeyRange?rn(this,a):dn(this.h.delete(a))};
k.get=function(a){return dn(this.h.get(a))};
k.index=function(a){try{return new tn(this.h.index(a))}catch(b){if(b instanceof Error&&"NotFoundError"===b.name)throw new Rm(a,this.h.name);throw b;}};
k.getName=function(){return this.h.name};
k.keyPath=function(){return this.h.keyPath};
function sn(a,b,c){a=a.h.openCursor(b.query,b.direction);return un(a).then(function(d){return en(d,c)})}
function mn(a){var b=this;this.h=a;this.j=new Map;this.i=!1;this.done=new Promise(function(c,d){b.h.addEventListener("complete",function(){c()});
b.h.addEventListener("error",function(e){e.currentTarget===e.target&&d(b.h.error)});
b.h.addEventListener("abort",function(){var e=b.h.error;if(e)d(e);else if(!b.i){e=Pm;for(var f=b.h.objectStoreNames,g=[],h=0;h<f.length;h++){var l=f.item(h);if(null===l)throw Error("Invariant: item in DOMStringList is null");g.push(l)}e=new e("UNKNOWN_ABORT",{objectStoreNames:g.join(),dbName:b.h.db.name,mode:b.h.mode});d(e)}})})}
function nn(a,b){var c=new Promise(function(d,e){try{b(a).then(function(f){d(f)}).catch(e)}catch(f){e(f),a.abort()}});
return Promise.all([c,a.done]).then(function(d){return p(d).next().value})}
mn.prototype.abort=function(){this.h.abort();this.i=!0;throw new Pm("EXPLICIT_ABORT");};
mn.prototype.objectStore=function(a){a=this.h.objectStore(a);var b=this.j.get(a);b||(b=new kn(a),this.j.set(a,b));return b};
function tn(a){this.h=a}
k=tn.prototype;k.count=function(a){return dn(this.h.count(a))};
k.delete=function(a){return vn(this,{query:a},function(b){return b.delete().then(function(){return b.continue()})})};
k.get=function(a){return dn(this.h.get(a))};
k.getKey=function(a){return dn(this.h.getKey(a))};
k.keyPath=function(){return this.h.keyPath};
k.unique=function(){return this.h.unique};
function vn(a,b,c){a=a.h.openCursor(void 0===b.query?null:b.query,void 0===b.direction?"next":b.direction);return un(a).then(function(d){return en(d,c)})}
function wn(a,b){this.request=a;this.cursor=b}
function un(a){return dn(a).then(function(b){return b?new wn(a,b):null})}
k=wn.prototype;k.advance=function(a){this.cursor.advance(a);return un(this.request)};
k.continue=function(a){this.cursor.continue(a);return un(this.request)};
k.delete=function(){return dn(this.cursor.delete()).then(function(){})};
k.getKey=function(){return this.cursor.key};
k.getValue=function(){return this.cursor.value};
k.update=function(a){return dn(this.cursor.update(a))};function xn(a,b,c){return new Promise(function(d,e){function f(){w||(w=new gn(g.result,{closed:r}));return w}
var g=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);var h=c.Gc,l=c.blocking,m=c.wd,q=c.upgrade,r=c.closed,w;g.addEventListener("upgradeneeded",function(t){try{if(null===t.newVersion)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(null===g.transaction)throw Error("Invariant: transaction on IDbOpenDbRequest is null");t.dataLoss&&"none"!==t.dataLoss&&Gm("IDB_DATA_CORRUPTED",{reason:t.dataLossMessage||"unknown reason",dbName:Im(a)});var A=f(),E=new mn(g.transaction);
q&&q(A,function(F){return t.oldVersion<F&&t.newVersion>=F},E);
E.done.catch(function(F){e(F)})}catch(F){e(F)}});
g.addEventListener("success",function(){var t=g.result;l&&t.addEventListener("versionchange",function(){l(f())});
t.addEventListener("close",function(){Gm("IDB_UNEXPECTEDLY_CLOSED",{dbName:Im(a),dbVersion:t.version});m&&m()});
d(f())});
g.addEventListener("error",function(){e(g.error)});
h&&g.addEventListener("blocked",function(){h()})})}
function yn(a,b,c){c=void 0===c?{}:c;return xn(a,b,c)}
function zn(a,b){b=void 0===b?{}:b;var c,d,e,f;return x(function(g){if(1==g.h)return za(g,2),c=self.indexedDB.deleteDatabase(a),d=b,(e=d.Gc)&&c.addEventListener("blocked",function(){e()}),v(g,cn(c),4);
if(2!=g.h)return Aa(g,0);f=Ba(g);throw Tm(f,a,"",-1);})}
;function An(a){return new Promise(function(b){pm(function(){b()},a)})}
function Bn(a,b){this.name=a;this.options=b;this.l=!0;this.o=this.m=0;this.i=500}
Bn.prototype.j=function(a,b,c){c=void 0===c?{}:c;return yn(a,b,c)};
Bn.prototype.delete=function(a){a=void 0===a?{}:a;return zn(this.name,a)};
function Cn(a,b){return new Pm("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
function Dn(a,b){if(!b)throw Um("openWithToken",Im(a.name));return En(a)}
function En(a){function b(){var f,g,h,l,m,q,r,w,t,A;return x(function(E){switch(E.h){case 1:return g=null!=(f=Error().stack)?f:"",za(E,2),v(E,a.j(a.name,a.options.version,d),4);case 4:h=E.i;for(var F=a.options,O=[],N=p(Object.keys(F.Da)),R=N.next();!R.done;R=N.next()){R=R.value;var ca=F.Da[R],U=void 0===ca.gd?Number.MAX_VALUE:ca.gd;!(h.h.version>=ca.Ia)||h.h.version>=U||h.h.objectStoreNames.contains(R)||O.push(R)}l=O;if(0===l.length){E.u(5);break}m=Object.keys(a.options.Da);q=h.objectStoreNames();
if(a.o<Uk("ytidb_reopen_db_retries",0))return a.o++,h.close(),Fm(new Pm("DB_REOPENED_BY_MISSING_OBJECT_STORES",{dbName:a.name,expectedObjectStores:m,foundObjectStores:q})),E.return(b());if(!(a.m<Uk("ytidb_remake_db_retries",1))){E.u(6);break}a.m++;if(!M("ytidb_remake_db_enable_backoff_delay")){E.u(7);break}return v(E,An(a.i),8);case 8:a.i*=2;case 7:return v(E,a.delete(),9);case 9:return Fm(new Pm("DB_DELETED_BY_MISSING_OBJECT_STORES",{dbName:a.name,expectedObjectStores:m,foundObjectStores:q})),E.return(b());
case 6:throw new Qm(q,m);case 5:return E.return(h);case 2:r=Ba(E);if(r instanceof DOMException?"VersionError"!==r.name:"DOMError"in self&&r instanceof DOMError?"VersionError"!==r.name:!(r instanceof Object&&"message"in r)||"An attempt was made to open a database using a lower version than the existing version."!==r.message){E.u(10);break}return v(E,a.j(a.name,void 0,Object.assign({},d,{upgrade:void 0})),11);case 11:w=E.i;t=w.h.version;if(void 0!==a.options.version&&t>a.options.version+1)throw w.close(),
a.l=!1,Cn(a,t);return E.return(w);case 10:throw c(),r instanceof Error&&!M("ytidb_async_stack_killswitch")&&(r.stack=r.stack+"\n"+g.substring(g.indexOf("\n")+1)),Tm(r,a.name,"",null!=(A=a.options.version)?A:-1);}})}
function c(){a.h===e&&(a.h=void 0)}
if(!a.l)throw Cn(a);if(a.h)return a.h;var d={blocking:function(f){f.close()},
closed:c,wd:c,upgrade:a.options.upgrade};var e=b();a.h=e;return a.h}
;var Fn=new Bn("YtIdbMeta",{Da:{databases:{Ia:1}},upgrade:function(a,b){b(1)&&jn(a,"databases",{keyPath:"actualName"})}});
function Gn(a,b){var c;return x(function(d){if(1==d.h)return v(d,Dn(Fn,b),2);c=d.i;return d.return(hn(c,["databases"],{R:!0,mode:"readwrite"},function(e){var f=e.objectStore("databases");return f.get(a.actualName).then(function(g){if(g?a.actualName!==g.actualName||a.publicName!==g.publicName||a.userIdentifier!==g.userIdentifier:1)return dn(f.h.put(a,void 0)).then(function(){})})}))})}
function Hn(a,b){var c;return x(function(d){if(1==d.h)return a?v(d,Dn(Fn,b),2):d.return();c=d.i;return d.return(c.delete("databases",a))})}
function In(a,b){var c,d;return x(function(e){return 1==e.h?(c=[],v(e,Dn(Fn,b),2)):3!=e.h?(d=e.i,v(e,hn(d,["databases"],{R:!0,mode:"readonly"},function(f){c.length=0;return sn(f.objectStore("databases"),{},function(g){a(g.getValue())&&c.push(g.getValue());return g.continue()})}),3)):e.return(c)})}
function Jn(a){return In(function(b){return"LogsDatabaseV2"===b.publicName&&void 0!==b.userIdentifier},a)}
function Kn(a,b,c){return In(function(d){return c?void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)&&c.includes(d.publicName):void 0!==d.userIdentifier&&!a.includes(d.userIdentifier)},b)}
function Ln(a){var b,c;return x(function(d){if(1==d.h)return b=um("YtIdbMeta hasAnyMeta other"),v(d,In(function(e){return void 0!==e.userIdentifier&&e.userIdentifier!==b},a),2);
c=d.i;return d.return(0<c.length)})}
;var Mn,Nn=new function(){}(new function(){});
function On(){var a,b,c,d;return x(function(e){switch(e.h){case 1:a=xm();if(null==(b=a)?0:b.hasSucceededOnce)return e.return(!0);var f;if(f=Hl)f=/WebKit\/([0-9]+)/.exec(Ub()),f=!!(f&&600<=parseInt(f[1],10));f&&(f=/WebKit\/([0-9]+)/.exec(Ub()),f=!(f&&602<=parseInt(f[1],10)));if(f||Lc)return e.return(!1);try{if(c=self,!(c.indexedDB&&c.IDBIndex&&c.IDBKeyRange&&c.IDBObjectStore))return e.return(!1)}catch(g){return e.return(!1)}if(!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return e.return(!1);
za(e,2);d={actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0};return v(e,Gn(d,Nn),4);case 4:return v(e,Hn("yt-idb-test-do-not-use",Nn),5);case 5:return e.return(!0);case 2:return Ba(e),e.return(!1)}})}
function Pn(){if(void 0!==Mn)return Mn;Am=!0;return Mn=On().then(function(a){Am=!1;var b;if(null!=(b=wm())&&b.h){var c;b={hasSucceededOnce:(null==(c=xm())?void 0:c.hasSucceededOnce)||a};var d;null==(d=wm())||d.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0)}return a})}
function Qn(){return B("ytglobal.idbToken_")||void 0}
function Rn(){var a=Qn();return a?Promise.resolve(a):Pn().then(function(b){(b=b?Nn:void 0)&&z("ytglobal.idbToken_",b);return b})}
;var Sn=0;function Tn(a,b){Sn||(Sn=fi.S(function(){var c,d,e,f,g;return x(function(h){switch(h.h){case 1:return v(h,Rn(),2);case 2:c=h.i;if(!c)return h.return();d=!0;za(h,3);return v(h,Kn(a,c,b),5);case 5:e=h.i;if(!e.length){d=!1;h.u(6);break}f=e[0];return v(h,zn(f.actualName),7);case 7:return v(h,Hn(f.actualName,c),6);case 6:Aa(h,4);break;case 3:g=Ba(h),Fm(g),d=!1;case 4:fi.ea(Sn),Sn=0,d&&Tn(a,b),h.h=0}})}))}
function Un(){var a;return x(function(b){return 1==b.h?v(b,Rn(),2):(a=b.i)?b.return(Ln(a)):b.return(!1)})}
new Fh;function Vn(a){if(!tm())throw a=new Pm("AUTH_INVALID",{dbName:a}),Fm(a),a;var b=um();return{actualName:a+":"+b,publicName:a,userIdentifier:b}}
function Wn(a,b,c,d){var e,f,g,h,l,m;return x(function(q){switch(q.h){case 1:return f=null!=(e=Error().stack)?e:"",v(q,Rn(),2);case 2:g=q.i;if(!g)throw h=Um("openDbImpl",a,b),M("ytidb_async_stack_killswitch")||(h.stack=h.stack+"\n"+f.substring(f.indexOf("\n")+1)),Fm(h),h;Hm(a);l=c?{actualName:a,publicName:a,userIdentifier:void 0}:Vn(a);za(q,3);return v(q,Gn(l,g),5);case 5:return v(q,yn(l.actualName,b,d),6);case 6:return q.return(q.i);case 3:return m=Ba(q),za(q,7),v(q,Hn(l.actualName,g),9);case 9:Aa(q,
8);break;case 7:Ba(q);case 8:throw m;}})}
function Xn(a,b,c){c=void 0===c?{}:c;return Wn(a,b,!1,c)}
function Yn(a,b,c){c=void 0===c?{}:c;return Wn(a,b,!0,c)}
function Zn(a,b){b=void 0===b?{}:b;var c,d;return x(function(e){if(1==e.h)return v(e,Rn(),2);if(3!=e.h){c=e.i;if(!c)return e.return();Hm(a);d=Vn(a);return v(e,zn(d.actualName,b),3)}return v(e,Hn(d.actualName,c),0)})}
function $n(a,b,c){a=a.map(function(d){return x(function(e){return 1==e.h?v(e,zn(d.actualName,b),2):v(e,Hn(d.actualName,c),0)})});
return Promise.all(a).then(function(){})}
function ao(){var a=void 0===a?{}:a;var b,c;return x(function(d){if(1==d.h)return v(d,Rn(),2);if(3!=d.h){b=d.i;if(!b)return d.return();Hm("LogsDatabaseV2");return v(d,Jn(b),3)}c=d.i;return v(d,$n(c,a,b),0)})}
function bo(a,b){b=void 0===b?{}:b;var c;return x(function(d){if(1==d.h)return v(d,Rn(),2);if(3!=d.h){c=d.i;if(!c)return d.return();Hm(a);return v(d,zn(a,b),3)}return v(d,Hn(a,c),0)})}
;function co(a,b){Bn.call(this,a,b);this.options=b;Hm(a)}
u(co,Bn);function eo(a,b){var c;return function(){c||(c=new co(a,b));return c}}
co.prototype.j=function(a,b,c){c=void 0===c?{}:c;return(this.options.pb?Yn:Xn)(a,b,Object.assign({},c))};
co.prototype.delete=function(a){a=void 0===a?{}:a;return(this.options.pb?bo:Zn)(this.name,a)};
function fo(a,b){return eo(a,b)}
;var go={},ho=fo("ytGcfConfig",{Da:(go.coldConfigStore={Ia:1},go.hotConfigStore={Ia:1},go),pb:!1,upgrade:function(a,b){b(1)&&(qn(jn(a,"hotConfigStore",{keyPath:"key",autoIncrement:!0}),"hotTimestampIndex","timestamp"),qn(jn(a,"coldConfigStore",{keyPath:"key",autoIncrement:!0}),"coldTimestampIndex","timestamp"))},
version:1});function io(a){return Dn(ho(),a)}
function jo(a,b,c){var d,e,f;return x(function(g){switch(g.h){case 1:return d={config:a,hashData:b,timestamp:Q()},v(g,io(c),2);case 2:return e=g.i,v(g,e.clear("hotConfigStore"),3);case 3:return v(g,ln(e,"hotConfigStore",d),4);case 4:return f=g.i,g.return(f)}})}
function ko(a,b,c,d){var e,f,g;return x(function(h){switch(h.h){case 1:return e={config:a,hashData:b,configData:c,timestamp:Q()},v(h,io(d),2);case 2:return f=h.i,v(h,f.clear("coldConfigStore"),3);case 3:return v(h,ln(f,"coldConfigStore",e),4);case 4:return g=h.i,h.return(g)}})}
function lo(a){var b,c;return x(function(d){return 1==d.h?v(d,io(a),2):3!=d.h?(b=d.i,c=void 0,v(d,hn(b,["coldConfigStore"],{mode:"readwrite",R:!0},function(e){return vn(e.objectStore("coldConfigStore").index("coldTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
function mo(a){var b,c;return x(function(d){return 1==d.h?v(d,io(a),2):3!=d.h?(b=d.i,c=void 0,v(d,hn(b,["hotConfigStore"],{mode:"readwrite",R:!0},function(e){return vn(e.objectStore("hotConfigStore").index("hotTimestampIndex"),{direction:"prev"},function(f){c=f.getValue()})}),3)):d.return(c)})}
;function no(){}
function oo(a,b,c){var d,e,f;return x(function(g){if(1==g.h){if(!M("gcf_config_store_update_enabled"))return g.u(0);c&&(a.h=c,z("yt.gcf.config.hotConfigGroup",a.h));a.hotHashData=b;z("yt.gcf.config.hotHashData",a.hotHashData);return(d=Qn())?c?g.u(4):v(g,mo(d),5):g.u(0)}4!=g.h&&(e=g.i,c=null==(f=e)?void 0:f.config);return v(g,jo(c,b,d),0)})}
function po(a,b,c){var d,e,f,g;return x(function(h){if(1==h.h){if(!M("gcf_config_store_update_enabled"))return h.u(0);a.coldHashData=b;z("yt.gcf.config.coldHashData",a.coldHashData);return(d=Qn())?c?h.u(4):v(h,lo(d),5):h.u(0)}4!=h.h&&(e=h.i,c=null==(f=e)?void 0:f.config);if(!c)return h.u(0);g=c.configData;return v(h,ko(c,b,g,d),0)})}
;function qo(){return"INNERTUBE_API_KEY"in Qk&&"INNERTUBE_API_VERSION"in Qk}
function ro(){return{innertubeApiKey:L("INNERTUBE_API_KEY"),innertubeApiVersion:L("INNERTUBE_API_VERSION"),yb:L("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),cc:L("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),Tc:L("INNERTUBE_CONTEXT_CLIENT_NAME",1),innertubeContextClientVersion:L("INNERTUBE_CONTEXT_CLIENT_VERSION"),ec:L("INNERTUBE_CONTEXT_HL"),dc:L("INNERTUBE_CONTEXT_GL"),Uc:L("INNERTUBE_HOST_OVERRIDE")||"",Wc:!!L("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),Vc:!!L("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:L("SERIALIZED_CLIENT_CONFIG_DATA")}}
function so(a){var b={client:{hl:a.ec,gl:a.dc,clientName:a.cc,clientVersion:a.innertubeContextClientVersion,configInfo:a.yb}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=y.devicePixelRatio;c&&1!=c&&(b.client.screenDensityFloat=String(c));c=Vk();""!==c&&(b.client.experimentsToken=c);c=Wk();0<c.length&&(b.request={internalExperimentFlags:c});to(a,void 0,b);M("enable_third_party_info")&&uo(void 0,b);vo(void 0,b);wo(a,void 0,b);xo(void 0,b);M("start_sending_config_hash")&&
yo(void 0,b);L("DELEGATED_SESSION_ID")&&!M("pageid_as_header_web")&&(b.user={onBehalfOfUser:L("DELEGATED_SESSION_ID")});a=Object;c=a.assign;for(var d=b.client,e={},f=p(Object.entries(kl(L("DEVICE","")))),g=f.next();!g.done;g=f.next()){var h=p(g.value);g=h.next().value;h=h.next().value;"cbrand"===g?e.deviceMake=h:"cmodel"===g?e.deviceModel=h:"cbr"===g?e.browserName=h:"cbrver"===g?e.browserVersion=h:"cos"===g?e.osName=h:"cosver"===g?e.osVersion=h:"cplatform"===g&&(e.platform=h)}b.client=c.call(a,d,
e);return b}
function zo(a){var b=new lj,c=new cj;D(c,1,a.ec);D(c,2,a.dc);D(c,16,a.Tc);D(c,17,a.innertubeContextClientVersion);if(a.yb){var d=a.yb,e=new Zi;d.coldConfigData&&D(e,1,d.coldConfigData);d.appInstallData&&D(e,6,d.appInstallData);d.coldHashData&&D(e,3,d.coldHashData);d.hotHashData&&D(e,5,d.hotHashData);G(c,Zi,62,e)}(d=y.devicePixelRatio)&&1!=d&&D(c,65,d);d=Vk();""!==d&&D(c,54,d);d=Wk();if(0<d.length){e=new ej;for(var f=0;f<d.length;f++){var g=new Xi;D(g,1,d[f].key);Wd(g,2,Yi,d[f].value);de(e,15,Xi,g)}G(b,
ej,5,e)}to(a,c);M("enable_third_party_info")&&uo(b);vo(c);wo(a,c);xo(c);M("start_sending_config_hash")&&yo(c);L("DELEGATED_SESSION_ID")&&!M("pageid_as_header_web")&&(a=new jj,D(a,3,L("DELEGATED_SESSION_ID")));a=p(Object.entries(kl(L("DEVICE",""))));for(d=a.next();!d.done;d=a.next())e=p(d.value),d=e.next().value,e=e.next().value,"cbrand"===d?D(c,12,e):"cmodel"===d?D(c,13,e):"cbr"===d?D(c,87,e):"cbrver"===d?D(c,88,e):"cos"===d?D(c,18,e):"cosver"===d?D(c,19,e):"cplatform"===d&&D(c,42,e);b.i(c);return b}
function to(a,b,c){a=a.cc;if("WEB"===a||"MWEB"===a||1===a||2===a)if(b){c=Yd(b,$i,96)||new $i;var d=Wl();d=Object.keys(sj).indexOf(d);d=-1===d?null:d;null!==d&&D(c,3,d);G(b,$i,96,c)}else c&&(c.client.mainAppWebInfo=null!=(d=c.client.mainAppWebInfo)?d:{},c.client.mainAppWebInfo.webDisplayMode=Wl())}
function uo(a,b){var c=B("yt.embedded_player.embed_url");c&&(a?(b=Yd(a,gj,7)||new gj,D(b,4,c),G(a,gj,7,b)):b&&(b.thirdParty={embedUrl:c}))}
function vo(a,b){var c;if(M("web_log_memory_total_kbytes")&&(null==(c=y.navigator)?0:c.deviceMemory)){var d;c=null==(d=y.navigator)?void 0:d.deviceMemory;a?D(a,95,1E6*c):b&&(b.client.memoryTotalKbytes=""+1E6*c)}}
function wo(a,b,c){if(a.appInstallData)if(b){var d;c=null!=(d=Yd(b,Zi,62))?d:new Zi;D(c,6,a.appInstallData);G(b,Zi,62,c)}else c&&(c.client.configInfo=c.client.configInfo||{},c.client.configInfo.appInstallData=a.appInstallData)}
function xo(a,b){var c=km();c&&(a?D(a,61,gm[c]):b&&(b.client.connectionType=c));M("web_log_effective_connection_type")&&(c=lm())&&(a?D(a,94,hm[c]):b&&(b.client.effectiveConnectionType=c))}
function Ao(a,b,c){c=void 0===c?{}:c;var d={};L("EOM_VISITOR_DATA")?d={"X-Goog-EOM-Visitor-Id":L("EOM_VISITOR_DATA")}:d={"X-Goog-Visitor-Id":c.visitorData||L("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.vr||L("AUTHORIZATION"))||(a?b="Bearer "+B("gapi.auth.getToken")().ur:b=yg([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=L("SESSION_INDEX",0),M("pageid_as_header_web")&&(d["X-Goog-PageId"]=L("DELEGATED_SESSION_ID")));return d}
function yo(a,b){no.h||(no.h=new no);var c=B("yt.gcf.config.coldConfigData");var d=B("yt.gcf.config.hotHashData");var e=B("yt.gcf.config.coldHashData");if(c&&e&&d)if(a){var f;b=null!=(f=Yd(a,Zi,62))?f:new Zi;D(b,1,c);D(b,3,e);D(b,5,d);G(a,Zi,62,b)}else b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.coldConfigData=c,b.client.configInfo.coldHashData=e,b.client.configInfo.hotHashData=d)}
;function Bo(a){a=Object.assign({},a);delete a.Authorization;var b=yg();if(b){var c=new li;c.update(L("INNERTUBE_API_KEY"));c.update(b);a.hash=cd(c.digest(),3)}return a}
;var Co;function Do(){Co||(Co=new vm("yt.innertube"));return Co}
function Eo(a,b,c,d){if(d)return null;d=Do().get("nextId",!0)||1;var e=Do().get("requests",!0)||{};e[d]={method:a,request:b,authState:Bo(c),requestTime:Math.round(Q())};Do().set("nextId",d+1,86400,!0);Do().set("requests",e,86400,!0);return d}
function Fo(a){var b=Do().get("requests",!0)||{};delete b[a];Do().set("requests",b,86400,!0)}
function Go(a){var b=Do().get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(Q())-d.requestTime)){var e=d.authState,f=Bo(Ao(!1));vb(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(Q())),Ho(a,d.method,e,{}));delete b[c]}}Do().set("requests",b,86400,!0)}}
;function Io(a){this.bb=this.h=!1;this.potentialEsfErrorCounter=this.i=0;this.handleError=function(){};
this.Ca=function(){};
this.now=Date.now;this.Ja=!1;var b;this.tc=null!=(b=a.tc)?b:100;var c;this.oc=null!=(c=a.oc)?c:1;var d;this.mc=null!=(d=a.mc)?d:2592E6;var e;this.kc=null!=(e=a.kc)?e:12E4;var f;this.nc=null!=(f=a.nc)?f:5E3;var g;this.H=null!=(g=a.H)?g:void 0;this.gb=!!a.gb;var h;this.fb=null!=(h=a.fb)?h:.1;var l;this.lb=null!=(l=a.lb)?l:10;a.handleError&&(this.handleError=a.handleError);a.Ca&&(this.Ca=a.Ca);a.Ja&&(this.Ja=a.Ja);a.bb&&(this.bb=a.bb);this.J=a.J;this.Z=a.Z;this.N=a.N;this.L=a.L;this.ja=a.ja;this.Eb=
a.Eb;this.Db=a.Db;Jo(this)&&(!this.J||this.J("networkless_logging"))&&Ko(this)}
function Ko(a){Jo(a)&&!a.Ja&&(a.h=!0,a.gb&&Math.random()<=a.fb&&a.N.Ic(a.H),Lo(a),a.L.U()&&a.Qa(),a.L.ia(a.Eb,a.Qa.bind(a)),a.L.ia(a.Db,a.Rb.bind(a)))}
k=Io.prototype;k.writeThenSend=function(a,b){var c=this;b=void 0===b?{}:b;if(Jo(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.N.set(d,this.H).then(function(e){d.id=e;c.L.U()&&Mo(c,d)}).catch(function(e){Mo(c,d);
No(c,e)})}else this.ja(a,b)};
k.sendThenWrite=function(a,b,c){var d=this;b=void 0===b?{}:b;if(Jo(this)&&this.h){var e={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.J&&this.J("nwl_skip_retry")&&(e.skipRetry=c);if(this.L.U()||this.J&&this.J("nwl_aggressive_send_then_write")&&!e.skipRetry){if(!e.skipRetry){var f=b.onError?b.onError:function(){};
b.onError=function(g,h){return x(function(l){if(1==l.h)return v(l,d.N.set(e,d.H).catch(function(m){No(d,m)}),2);
f(g,h);l.h=0})}}this.ja(a,b,e.skipRetry)}else this.N.set(e,this.H).catch(function(g){d.ja(a,b,e.skipRetry);
No(d,g)})}else this.ja(a,b,this.J&&this.J("nwl_skip_retry")&&c)};
k.sendAndWrite=function(a,b){var c=this;b=void 0===b?{}:b;if(Jo(this)&&this.h){var d={url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0},e=!1,f=b.onSuccess?b.onSuccess:function(){};
d.options.onSuccess=function(g,h){void 0!==d.id?c.N.Ba(d.id,c.H):e=!0;c.L.wa&&c.J&&c.J("vss_network_hint")&&c.L.wa(!0);f(g,h)};
this.ja(d.url,d.options);this.N.set(d,this.H).then(function(g){d.id=g;e&&c.N.Ba(d.id,c.H)}).catch(function(g){No(c,g)})}else this.ja(a,b)};
k.Qa=function(){var a=this;if(!Jo(this))throw Um("throttleSend");this.i||(this.i=this.Z.S(function(){var b;return x(function(c){if(1==c.h)return v(c,a.N.ac("NEW",a.H),2);if(3!=c.h)return b=c.i,b?v(c,Mo(a,b),3):(a.Rb(),c.return());a.i&&(a.i=0,a.Qa());c.h=0})},this.tc))};
k.Rb=function(){this.Z.ea(this.i);this.i=0};
function Mo(a,b){var c,d;return x(function(e){switch(e.h){case 1:if(!Jo(a))throw c=Um("immediateSend"),c;if(void 0===b.id){e.u(2);break}return v(e,a.N.Yc(b.id,a.H),3);case 3:(d=e.i)?b=d:a.Ca(Error("The request cannot be found in the database."));case 2:if(Oo(a,b,a.mc)){e.u(4);break}a.Ca(Error("Networkless Logging: Stored logs request expired age limit"));if(void 0===b.id){e.u(5);break}return v(e,a.N.Ba(b.id,a.H),5);case 5:return e.return();case 4:b.skipRetry||(b=Po(a,b));if(!b){e.u(0);break}if(!b.skipRetry||
void 0===b.id){e.u(8);break}return v(e,a.N.Ba(b.id,a.H),8);case 8:a.ja(b.url,b.options,!!b.skipRetry),e.h=0}})}
function Po(a,b){if(!Jo(a))throw Um("updateRequestHandlers");var c=b.options.onError?b.options.onError:function(){};
b.options.onError=function(e,f){var g,h,l;return x(function(m){switch(m.h){case 1:g=Qo(f);if(!(a.J&&a.J("nwl_consider_error_code")&&g||a.J&&!a.J("nwl_consider_error_code")&&a.potentialEsfErrorCounter<=a.lb)){m.u(2);break}if(!a.L.ob){m.u(3);break}return v(m,a.L.ob(),3);case 3:if(a.L.U()){m.u(2);break}c(e,f);if(!a.J||!a.J("nwl_consider_error_code")||void 0===(null==(h=b)?void 0:h.id)){m.u(6);break}return v(m,a.N.Ib(b.id,a.H,!1),6);case 6:return m.return();case 2:if(a.J&&a.J("nwl_consider_error_code")&&
!g&&a.potentialEsfErrorCounter>a.lb)return m.return();a.potentialEsfErrorCounter++;if(void 0===(null==(l=b)?void 0:l.id)){m.u(8);break}return b.sendCount<a.oc?v(m,a.N.Ib(b.id,a.H),12):v(m,a.N.Ba(b.id,a.H),8);case 12:a.Z.S(function(){a.L.U()&&a.Qa()},a.nc);
case 8:c(e,f),m.h=0}})};
var d=b.options.onSuccess?b.options.onSuccess:function(){};
b.options.onSuccess=function(e,f){var g;return x(function(h){if(1==h.h)return void 0===(null==(g=b)?void 0:g.id)?h.u(2):v(h,a.N.Ba(b.id,a.H),2);a.L.wa&&a.J&&a.J("vss_network_hint")&&a.L.wa(!0);d(e,f);h.h=0})};
return b}
function Oo(a,b,c){b=b.timestamp;return a.now()-b>=c?!1:!0}
function Lo(a){if(!Jo(a))throw Um("retryQueuedRequests");a.N.ac("QUEUED",a.H).then(function(b){b&&!Oo(a,b,a.kc)?a.Z.S(function(){return x(function(c){if(1==c.h)return void 0===b.id?c.u(2):v(c,a.N.Ib(b.id,a.H),2);Lo(a);c.h=0})}):a.L.U()&&a.Qa()})}
function No(a,b){a.yc&&!a.L.U()?a.yc(b):a.handleError(b)}
function Jo(a){return!!a.H||a.bb}
function Qo(a){var b;return(a=null==a?void 0:null==(b=a.error)?void 0:b.code)&&400<=a&&599>=a?!1:!0}
;function Ro(a,b){this.version=a;this.args=b}
;function So(a,b){this.topic=a;this.h=b}
So.prototype.toString=function(){return this.topic};var To=B("ytPubsub2Pubsub2Instance")||new K;K.prototype.subscribe=K.prototype.subscribe;K.prototype.unsubscribeByKey=K.prototype.Ga;K.prototype.publish=K.prototype.sa;K.prototype.clear=K.prototype.clear;z("ytPubsub2Pubsub2Instance",To);var Uo=B("ytPubsub2Pubsub2SubscribedKeys")||{};z("ytPubsub2Pubsub2SubscribedKeys",Uo);var Vo=B("ytPubsub2Pubsub2TopicToKeys")||{};z("ytPubsub2Pubsub2TopicToKeys",Vo);var Wo=B("ytPubsub2Pubsub2IsAsync")||{};z("ytPubsub2Pubsub2IsAsync",Wo);
z("ytPubsub2Pubsub2SkipSubKey",null);function Xo(a,b){var c=Yo();c&&c.publish.call(c,a.toString(),a,b)}
function Zo(a){var b=$o,c=Yo();if(!c)return 0;var d=c.subscribe(b.toString(),function(e,f){var g=B("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=function(){if(Uo[d])try{if(f&&b instanceof So&&b!=e)try{var h=b.h,l=f;if(!l.args||!l.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");try{if(!h.qa){var m=new h;h.qa=m.version}var q=h.qa}catch(F){}if(!q||l.version!=q)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{q=Reflect;var r=q.construct;
var w=l.args,t=w.length;if(0<t){var A=Array(t);for(l=0;l<t;l++)A[l]=w[l];var E=A}else E=[];f=r.call(q,h,E)}catch(F){throw F.message="yt.pubsub2.Data.deserialize(): "+F.message,F;}}catch(F){throw F.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+F.message,F;}a.call(window,f)}catch(F){cl(F)}},Wo[b.toString()]?B("yt.scheduler.instance")?fi.S(g):tl(g,0):g())});
Uo[d]=!0;Vo[b.toString()]||(Vo[b.toString()]=[]);Vo[b.toString()].push(d);return d}
function ap(){var a=bp,b=Zo(function(c){a.apply(void 0,arguments);cp(b)});
return b}
function cp(a){var b=Yo();b&&("number"===typeof a&&(a=[a]),hb(a,function(c){b.unsubscribeByKey(c);delete Uo[c]}))}
function Yo(){return B("ytPubsub2Pubsub2Instance")}
;var dp;
function ep(){if(dp)return dp();var a={};dp=fo("LogsDatabaseV2",{Da:(a.LogsRequestsStore={Ia:2},a),pb:!1,upgrade:function(b,c,d){c(2)&&jn(b,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});c(3);c(5)&&(d=d.objectStore("LogsRequestsStore"),d.h.indexNames.contains("newRequest")&&d.h.deleteIndex("newRequest"),qn(d,"newRequestV2",["status","interface","timestamp"]));c(7)&&b.h.objectStoreNames.contains("sapisid")&&b.h.deleteObjectStore("sapisid");c(9)&&b.h.objectStoreNames.contains("SWHealthLog")&&b.h.deleteObjectStore("SWHealthLog")},
version:9});return dp()}
;function fp(a){return Dn(ep(),a)}
function gp(a,b){var c,d,e,f;return x(function(g){if(1==g.h)return c={startTime:Q(),transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},v(g,fp(b),2);if(3!=g.h)return d=g.i,e=Object.assign({},a,{options:JSON.parse(JSON.stringify(a.options)),interface:L("INNERTUBE_CONTEXT_CLIENT_NAME",0)}),v(g,ln(d,"LogsRequestsStore",e),3);f=g.i;c.yd=Q();hp(c);return g.return(f)})}
function ip(a,b){var c,d,e,f,g,h,l;return x(function(m){if(1==m.h)return c={startTime:Q(),transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},v(m,fp(b),2);if(3!=m.h)return d=m.i,e=L("INNERTUBE_CONTEXT_CLIENT_NAME",0),f=[a,e,0],g=[a,e,Q()],h=IDBKeyRange.bound(f,g),l=void 0,v(m,hn(d,["LogsRequestsStore"],{mode:"readwrite",R:!0},function(q){return vn(q.objectStore("LogsRequestsStore").index("newRequestV2"),{query:h,direction:"prev"},function(r){r.getValue()&&(l=r.getValue(),"NEW"===a&&(l.status="QUEUED",
r.update(l)))})}),3);
c.yd=Q();hp(c);return m.return(l)})}
function jp(a,b){var c;return x(function(d){if(1==d.h)return v(d,fp(b),2);c=d.i;return d.return(hn(c,["LogsRequestsStore"],{mode:"readwrite",R:!0},function(e){var f=e.objectStore("LogsRequestsStore");return f.get(a).then(function(g){if(g)return g.status="QUEUED",dn(f.h.put(g,void 0)).then(function(){return g})})}))})}
function kp(a,b,c){c=void 0===c?!0:c;var d;return x(function(e){if(1==e.h)return v(e,fp(b),2);d=e.i;return e.return(hn(d,["LogsRequestsStore"],{mode:"readwrite",R:!0},function(f){var g=f.objectStore("LogsRequestsStore");return g.get(a).then(function(h){return h?(h.status="NEW",c&&(h.sendCount+=1),dn(g.h.put(h,void 0)).then(function(){return h})):Ym.resolve(void 0)})}))})}
function lp(a,b){var c;return x(function(d){if(1==d.h)return v(d,fp(b),2);c=d.i;return d.return(c.delete("LogsRequestsStore",a))})}
function mp(a){var b,c;return x(function(d){if(1==d.h)return v(d,fp(a),2);b=d.i;c=Q()-2592E6;return v(d,hn(b,["LogsRequestsStore"],{mode:"readwrite",R:!0},function(e){return sn(e.objectStore("LogsRequestsStore"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return f.continue()})})}),0)})}
function np(){x(function(a){return v(a,ao(),0)})}
function hp(a){M("nwl_csi_killswitch")||.01>=Math.random()&&Xo("nwl_transaction_latency_payload",a)}
;var op={},pp=fo("ServiceWorkerLogsDatabase",{Da:(op.SWHealthLog={Ia:1},op),pb:!0,upgrade:function(a,b){b(1)&&qn(jn(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}),"swHealthNewRequest",["interface","timestamp"])},
version:1});function qp(a){return Dn(pp(),a)}
function rp(a){var b,c;x(function(d){if(1==d.h)return v(d,qp(a),2);b=d.i;c=Q()-2592E6;return v(d,hn(b,["SWHealthLog"],{mode:"readwrite",R:!0},function(e){return sn(e.objectStore("SWHealthLog"),{},function(f){if(f.getValue().timestamp<=c)return f.delete().then(function(){return f.continue()})})}),0)})}
function sp(a){var b;return x(function(c){if(1==c.h)return v(c,qp(a),2);b=c.i;return v(c,b.clear("SWHealthLog"),0)})}
;var tp={},up=0;function vp(a){var b=new Image,c=""+up++;tp[c]=b;b.onload=b.onerror=function(){delete tp[c]};
b.src=a}
;function wp(){this.h=new Map;this.i=!1}
function xp(){if(!wp.h){var a=B("yt.networkRequestMonitor.instance")||new wp;z("yt.networkRequestMonitor.instance",a);wp.h=a}return wp.h}
wp.prototype.requestComplete=function(a,b){b&&(this.i=!0);a=this.removeParams(a);this.h.get(a)||this.h.set(a,b)};
wp.prototype.isEndpointCFR=function(a){a=this.removeParams(a);return(a=this.h.get(a))?!1:!1===a&&this.i?!0:null};
wp.prototype.removeParams=function(a){return a.split("?")[0]};
wp.prototype.removeParams=wp.prototype.removeParams;wp.prototype.isEndpointCFR=wp.prototype.isEndpointCFR;wp.prototype.requestComplete=wp.prototype.requestComplete;wp.getInstance=xp;var yp;function zp(){yp||(yp=new vm("yt.offline"));return yp}
function Np(a){if(M("offline_error_handling")){var b=zp().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);zp().set("errors",b,2592E3,!0)}}
;function lq(){ef.call(this);var a=this;this.j=!1;this.i=ei();this.i.ia("networkstatus-online",function(){if(a.j&&M("offline_error_handling")){var b=zp().get("errors",!0);if(b){for(var c in b)if(b[c]){var d=new P(c,"sent via offline_errors");d.name=b[c].name;d.stack=b[c].stack;d.level=b[c].level;cl(d)}zp().set("errors",{},2592E3,!0)}}})}
u(lq,ef);function mq(){if(!lq.h){var a=B("yt.networkStatusManager.instance")||new lq;z("yt.networkStatusManager.instance",a);lq.h=a}return lq.h}
k=lq.prototype;k.U=function(){return this.i.U()};
k.wa=function(a){this.i.i=a};
k.Rc=function(){var a=window.navigator.onLine;return void 0===a?!0:a};
k.Mc=function(){this.j=!0};
k.ia=function(a,b){return this.i.ia(a,b)};
k.ob=function(a){a=ci(this.i,a);a.then(function(b){M("use_cfr_monitor")&&xp().requestComplete("generate_204",b)});
return a};
lq.prototype.sendNetworkCheckRequest=lq.prototype.ob;lq.prototype.listen=lq.prototype.ia;lq.prototype.enableErrorFlushing=lq.prototype.Mc;lq.prototype.getWindowStatus=lq.prototype.Rc;lq.prototype.networkStatusHint=lq.prototype.wa;lq.prototype.isNetworkAvailable=lq.prototype.U;lq.getInstance=mq;function nq(a){a=void 0===a?{}:a;ef.call(this);var b=this;this.i=this.o=0;this.j=mq();var c=B("yt.networkStatusManager.instance.listen").bind(this.j);c&&(a.nb?(this.nb=a.nb,c("networkstatus-online",function(){oq(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){oq(b,"publicytnetworkstatus-offline")})):(c("networkstatus-online",function(){ff(b,"publicytnetworkstatus-online")}),c("networkstatus-offline",function(){ff(b,"publicytnetworkstatus-offline")})))}
u(nq,ef);nq.prototype.U=function(){var a=B("yt.networkStatusManager.instance.isNetworkAvailable");return a?a.bind(this.j)():!0};
nq.prototype.wa=function(a){var b=B("yt.networkStatusManager.instance.networkStatusHint").bind(this.j);b&&b(a)};
nq.prototype.ob=function(a){var b=this,c;return x(function(d){c=B("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(b.j);return M("skip_network_check_if_cfr")&&xp().isEndpointCFR("generate_204")?d.return(new Promise(function(e){var f;b.wa((null==(f=window.navigator)?void 0:f.onLine)||!0);e(b.U())})):c?d.return(c(a)):d.return(!0)})};
function oq(a,b){a.nb?a.i?(fi.ea(a.o),a.o=fi.S(function(){a.m!==b&&(ff(a,b),a.m=b,a.i=Q())},a.nb-(Q()-a.i))):(ff(a,b),a.m=b,a.i=Q()):ff(a,b)}
;var pq;function qq(){var a=Io.call;pq||(pq=new nq({Hr:!0,Br:!0}));a.call(Io,this,{N:{Ic:mp,Ba:lp,ac:ip,Yc:jp,Ib:kp,set:gp},L:pq,handleError:cl,Ca:dl,ja:rq,now:Q,yc:Np,Z:sm(),Eb:"publicytnetworkstatus-online",Db:"publicytnetworkstatus-offline",gb:!0,fb:.1,lb:Uk("potential_esf_error_limit",10),J:M,Ja:!(tm()&&sq())});this.j=new Fh;M("networkless_immediately_drop_all_requests")&&np();bo("LogsDatabaseV2")}
u(qq,Io);function tq(){var a=B("yt.networklessRequestController.instance");a||(a=new qq,z("yt.networklessRequestController.instance",a),M("networkless_logging")&&Rn().then(function(b){a.H=b;Ko(a);a.j.resolve();a.gb&&Math.random()<=a.fb&&a.H&&rp(a.H);M("networkless_immediately_drop_sw_health_store")&&uq(a)}));
return a}
qq.prototype.writeThenSend=function(a,b){b||(b={});tm()||(this.h=!1);Io.prototype.writeThenSend.call(this,a,b)};
qq.prototype.sendThenWrite=function(a,b,c){b||(b={});tm()||(this.h=!1);Io.prototype.sendThenWrite.call(this,a,b,c)};
qq.prototype.sendAndWrite=function(a,b){b||(b={});tm()||(this.h=!1);Io.prototype.sendAndWrite.call(this,a,b)};
qq.prototype.awaitInitialization=function(){return this.j.promise};
function uq(a){var b;x(function(c){if(!a.H)throw b=Um("clearSWHealthLogsDb"),b;return c.return(sp(a.H).catch(function(d){a.handleError(d)}))})}
function rq(a,b,c){M("use_cfr_monitor")&&vq(a,b);if(M("use_request_time_ms_header"))b.headers&&(b.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(Q())));else{var d;if(null==(d=b.postParams)?0:d.requestTimeMs)b.postParams.requestTimeMs=Math.round(Q())}if(c&&0===Object.keys(b).length){var e=void 0===e?"":e;var f=void 0===f?!1:f;if(a)if(e)Cl(a,void 0,"POST",e);else if(L("USE_NET_AJAX_FOR_PING_TRANSPORT",!1))Cl(a,void 0,"GET","",void 0,void 0,f);else{b:{try{var g=new db({url:a});if(g.j&&g.i||
g.l){var h=nc(oc(5,a)),l;if(!(l=!h||!h.endsWith("/aclk"))){var m=a.search(Cc),q=yc(a,0,"ri",m);if(0>q)var r=null;else{var w=a.indexOf("&",q);if(0>w||w>m)w=m;r=decodeURIComponent(a.slice(q+3,-1!==w?w:0).replace(/\+/g," "))}l="1"!==r}var t=!l;break b}}catch(E){}t=!1}if(t){b:{try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,"")){var A=!0;break b}}catch(E){}A=!1}c=A?!0:!1}else c=!1;c||vp(a)}}else zl(a,b)}
function vq(a,b){var c=b.onError?b.onError:function(){};
b.onError=function(e,f){xp().requestComplete(a,!1);c(e,f)};
var d=b.onSuccess?b.onSuccess:function(){};
b.onSuccess=function(e,f){xp().requestComplete(a,!0);d(e,f)}}
function sq(){return"www.youtube-nocookie.com"!==pc(document.location.toString())}
;var wq=!1,xq=y.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:wq};z("ytNetworklessLoggingInitializationOptions",xq);function yq(){var a;x(function(b){if(1==b.h)return v(b,Rn(),2);a=b.i;if(!a||!tm()&&!M("nwl_init_require_datasync_id_killswitch")||!sq())return b.u(0);wq=!0;xq.isNwlInitialized=wq;return v(b,tq().awaitInitialization(),0)})}
;function zq(a){var b=this;this.config_=null;a?this.config_=a:qo()&&(this.config_=ro());nm(function(){Go(b)},5E3)}
zq.prototype.isReady=function(){!this.config_&&qo()&&(this.config_=ro());return!!this.config_};
function Ho(a,b,c,d){function e(A){A=void 0===A?!1:A;var E;if(d.retry&&"www.youtube-nocookie.com"!=h&&(A||M("skip_ls_gel_retry")||"application/json"!==g.headers["Content-Type"]||(E=Eo(b,c,m,l)),E)){var F=g.onSuccess,O=g.onFetchSuccess;g.onSuccess=function(N,R){Fo(E);F(N,R)};
c.onFetchSuccess=function(N,R){Fo(E);O(N,R)}}try{A&&d.retry&&!d.hc.bypassNetworkless?(g.method="POST",d.hc.writeThenSend?tq().writeThenSend(t,g):tq().sendAndWrite(t,g)):M("web_all_payloads_via_jspb")?zl(t,g):(g.method="POST",g.postParams||(g.postParams={}),zl(t,g))}catch(N){if("InvalidAccessError"==N.name)E&&(Fo(E),E=0),dl(Error("An extension is blocking network request."));
else throw N;}E&&nm(function(){Go(a)},5E3)}
!L("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&dl(new P("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var f=new P("innertube xhrclient not ready",b,c,d);cl(f);throw f;}var g={headers:d.headers||{},method:"POST",postParams:c,postBody:d.postBody,postBodyFormat:d.postBodyFormat||"JSON",onTimeout:function(){d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:function(A,E){if(d.onSuccess)d.onSuccess(E)},
onFetchSuccess:function(A){if(d.onSuccess)d.onSuccess(A)},
onError:function(A,E){if(d.onError)d.onError(E)},
onFetchError:function(A){if(d.onError)d.onError(A)},
timeout:d.timeout,withCredentials:!0};g.headers["Content-Type"]||(g.headers["Content-Type"]="application/json");var h="";(f=a.config_.Uc)&&(h=f);var l=a.config_.Wc||!1,m=Ao(l,h,d);Object.assign(g.headers,m);(f=g.headers.Authorization)&&!h&&(g.headers["x-origin"]=window.location.origin);var q="/youtubei/"+a.config_.innertubeApiVersion+"/"+b,r={alt:"json"},w=a.config_.Vc&&f;w=w&&f.startsWith("Bearer");w||(r.key=a.config_.innertubeApiKey);var t=ml(""+h+q,r||{},!0);(B("ytNetworklessLoggingInitializationOptions")?
xq.isNwlInitialized:wq)?Pn().then(function(A){e(A)}):e(!1)}
;var Aq=0,Bq=Nc?"webkit":Mc?"moz":Kc?"ms":Jc?"o":"";z("ytDomDomGetNextId",B("ytDomDomGetNextId")||function(){return++Aq});var Cq={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Dq(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.rotation=this.clientY=this.clientX=0;this.scale=1;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Cq||(this[b]=a[b]);this.scale=a.scale;this.rotation=a.rotation;var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;
if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(e){}}
function Eq(a){if(document.body&&document.documentElement){var b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
Dq.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Dq.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Dq.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var qb=y.ytEventsEventsListeners||{};z("ytEventsEventsListeners",qb);var Fq=y.ytEventsEventsCounter||{count:0};z("ytEventsEventsCounter",Fq);
function Gq(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return pb(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Sa(e[4])&&Sa(d)&&vb(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
var Hq=fb(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function Iq(a,b,c,d){d=void 0===d?{}:d;if(!a||!a.addEventListener&&!a.attachEvent)return"";var e=Gq(a,b,c,d);if(e)return e;e=++Fq.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Dq(h);if(!pf(h.relatedTarget,function(l){return l==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Dq(h);
h.currentTarget=a;return c.call(a,h)};
g=bl(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Hq()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);qb[e]=[a,b,c,g,d];return e}
function Jq(a){a&&("string"==typeof a&&(a=[a]),hb(a,function(b){if(b in qb){var c=qb[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Hq()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete qb[b]}}))}
;var Kq=window.ytcsi&&window.ytcsi.now?window.ytcsi.now:window.performance&&window.performance.timing&&window.performance.now&&window.performance.timing.navigationStart?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()};function Lq(a){this.F=a;this.i=null;this.m=0;this.s=null;this.o=0;this.j=[];for(a=0;4>a;a++)this.j.push(0);this.l=0;this.K=Iq(window,"mousemove",Za(this.O,this));a=Za(this.I,this);"function"===typeof a&&(a=bl(a));this.P=window.setInterval(a,25)}
ab(Lq,J);Lq.prototype.O=function(a){void 0===a.h&&Eq(a);var b=a.h;void 0===a.i&&Eq(a);this.i=new lf(b,a.i)};
Lq.prototype.I=function(){if(this.i){var a=Kq();if(0!=this.m){var b=this.s,c=this.i,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.m);this.j[this.l]=.5<Math.abs((d-this.o)/this.o)?1:0;for(c=b=0;4>c;c++)b+=this.j[c]||0;3<=b&&this.F();this.o=d}this.m=a;this.s=this.i;this.l=(this.l+1)%4}};
Lq.prototype.B=function(){window.clearInterval(this.P);Jq(this.K)};var Mq={};
function Nq(a){var b=void 0===a?{}:a;a=void 0===b.dd?!1:b.dd;b=void 0===b.Nc?!0:b.Nc;if(null==B("_lact",window)){var c=parseInt(L("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;z("_lact",c,window);z("_fact",c,window);-1==c&&Oq();Iq(document,"keydown",Oq);Iq(document,"keyup",Oq);Iq(document,"mousedown",Oq);Iq(document,"mouseup",Oq);a?Iq(window,"touchmove",function(){Pq("touchmove",200)},{passive:!0}):(Iq(window,"resize",function(){Pq("resize",200)}),b&&Iq(window,"scroll",function(){Pq("scroll",200)}));
new Lq(function(){Pq("mouse",100)});
Iq(document,"touchstart",Oq,{passive:!0});Iq(document,"touchend",Oq,{passive:!0})}}
function Pq(a,b){Mq[a]||(Mq[a]=!0,fi.S(function(){Oq();Mq[a]=!1},b))}
function Oq(){null==B("_lact",window)&&Nq();var a=Date.now();z("_lact",a,window);-1==B("_fact",window)&&z("_fact",a,window);(a=B("ytglobal.ytUtilActivityCallback_"))&&a()}
function Qq(){var a=B("_lact",window);return null==a?-1:Math.max(Date.now()-a,0)}
;var Rq=y.ytPubsubPubsubInstance||new K,Sq=y.ytPubsubPubsubSubscribedKeys||{},Tq=y.ytPubsubPubsubTopicToKeys||{},Uq=y.ytPubsubPubsubIsSynchronous||{};function Vq(a,b){var c=Wq();if(c&&b){var d=c.subscribe(a,function(){var e=arguments;var f=function(){Sq[d]&&b.apply&&"function"==typeof b.apply&&b.apply(window,e)};
try{Uq[a]?f():tl(f,0)}catch(g){cl(g)}},void 0);
Sq[d]=!0;Tq[a]||(Tq[a]=[]);Tq[a].push(d);return d}return 0}
function Xq(a){var b=Wq();b&&("number"===typeof a?a=[a]:"string"===typeof a&&(a=[parseInt(a,10)]),hb(a,function(c){b.unsubscribeByKey(c);delete Sq[c]}))}
function Yq(a,b){var c=Wq();c&&c.publish.apply(c,arguments)}
function Zq(a){var b=Wq();if(b)if(b.clear(a),a)$q(a);else for(var c in Tq)$q(c)}
function Wq(){return y.ytPubsubPubsubInstance}
function $q(a){Tq[a]&&(a=Tq[a],hb(a,function(b){Sq[b]&&delete Sq[b]}),a.length=0)}
K.prototype.subscribe=K.prototype.subscribe;K.prototype.unsubscribeByKey=K.prototype.Ga;K.prototype.publish=K.prototype.sa;K.prototype.clear=K.prototype.clear;z("ytPubsubPubsubInstance",Rq);z("ytPubsubPubsubTopicToKeys",Tq);z("ytPubsubPubsubIsSynchronous",Uq);z("ytPubsubPubsubSubscribedKeys",Sq);var ar=Symbol("injectionDeps");function br(a){this.name=a}
br.prototype.toString=function(){return"InjectionToken("+this.name+")"};
function cr(){this.key=dr}
function er(){this.h=new Map;this.i=new Map}
er.prototype.resolve=function(a){return a instanceof cr?fr(this,a.key,[],!0):fr(this,a,[])};
function fr(a,b,c,d){d=void 0===d?!1:d;if(-1<c.indexOf(b))throw Error("Deps cycle for: "+b);if(a.i.has(b))return a.i.get(b);if(!a.h.has(b)){if(d)return;throw Error("No provider for: "+b);}d=a.h.get(b);c.push(b);if(d.wc)var e=d.wc;else if(d.Bd)e=d[ar]?gr(a,d[ar],c):[],e=d.Bd.apply(d,ja(e));else if(d.vc){e=d.vc;var f=e[ar]?gr(a,e[ar],c):[];e=new (Function.prototype.bind.apply(e,[null].concat(ja(f))))}else throw Error("Could not resolve providers for: "+b);c.pop();d.Rr||a.i.set(b,e);return e}
function gr(a,b,c){return b?b.map(function(d){return d instanceof cr?fr(a,d.key,c,!0):fr(a,d,c)}):[]}
;var hr;function ir(){hr||(hr=new er);return hr}
;function jr(){this.store={};this.h={}}
jr.prototype.storePayload=function(a,b){a=kr(a);this.store[a]?this.store[a].push(b):(this.h={},this.store[a]=[b]);return a};
jr.prototype.extractMatchingEntries=function(a){a=lr(this,a);for(var b=[],c=0;c<a.length;c++)this.store[a[c]]&&(b.push.apply(b,ja(this.store[a[c]])),delete this.store[a[c]]);return b};
jr.prototype.getSequenceCount=function(a){a=lr(this,a);for(var b=0,c=0;c<a.length;c++)b+=this.store[a[c]].length||0;return b};
function lr(a,b){var c=kr(b);if(a.h[c])return a.h[c];var d=Object.keys(a.store)||[];if(1>=d.length&&kr(b)===d[0])return d;for(var e=[],f=0;f<d.length;f++){var g=d[f].split("/");if(mr(b.auth,g[0])){var h=b.isJspb;mr(void 0===h?"undefined":h?"true":"false",g[1])&&mr(b.cttAuthInfo,g[2])&&e.push(d[f])}}return a.h[c]=e}
function mr(a,b){return void 0===a||"undefined"===a?!0:a===b}
jr.prototype.getSequenceCount=jr.prototype.getSequenceCount;jr.prototype.extractMatchingEntries=jr.prototype.extractMatchingEntries;jr.prototype.storePayload=jr.prototype.storePayload;function kr(a){return[void 0===a.auth?"undefined":a.auth,void 0===a.isJspb?"undefined":a.isJspb,void 0===a.cttAuthInfo?"undefined":a.cttAuthInfo].join("/")}
;function nr(a,b){if(a)return a[b.name]}
;var or=Uk("initial_gel_batch_timeout",2E3),pr=Uk("gel_queue_timeout_max_ms",6E4),qr=Math.pow(2,16)-1,rr=void 0;function sr(){this.j=this.h=this.i=0}
var tr=new sr,ur=new sr,vr,wr=!0,xr=y.ytLoggingTransportGELQueue_||new Map;z("ytLoggingTransportGELQueue_",xr);var yr=y.ytLoggingTransportGELProtoQueue_||new Map;z("ytLoggingTransportGELProtoQueue_",yr);var zr=y.ytLoggingTransportTokensToCttTargetIds_||{};z("ytLoggingTransportTokensToCttTargetIds_",zr);var Ar=y.ytLoggingTransportTokensToJspbCttTargetIds_||{};z("ytLoggingTransportTokensToJspbCttTargetIds_",Ar);var Br={};function Cr(){var a=B("yt.logging.ims");a||(a=new jr,z("yt.logging.ims",a));return a}
function Dr(a,b){M("web_all_payloads_via_jspb")&&dl(new P("transport.log called for JSON in JSPB only experiment"));if("log_event"===a.endpoint){Er(a);var c=Fr(a);if(M("use_new_in_memory_storage")){Br[c]=!0;var d={cttAuthInfo:c,isJspb:!1};Cr().storePayload(d,a.payload);Gr(b,[],c,!1,d)}else d=xr.get(c)||[],xr.set(c,d),d.push(a.payload),Gr(b,d,c)}}
function Hr(a,b){if("log_event"===a.endpoint){Er(void 0,a);var c=Fr(a,!0);if(M("use_new_in_memory_storage")){Br[c]=!0;var d={cttAuthInfo:c,isJspb:!0};Cr().storePayload(d,a.payload.toJSON());Gr(b,[],c,!0,d)}else d=yr.get(c)||[],yr.set(c,d),a=a.payload.toJSON(),d.push(a),Gr(b,d,c,!0)}}
function Gr(a,b,c,d,e){d=void 0===d?!1:d;a&&(rr=new a);a=Uk("tvhtml5_logging_max_batch_ads_fork")||Uk("tvhtml5_logging_max_batch")||Uk("web_logging_max_batch")||100;var f=Q(),g=d?ur.j:tr.j;b=b.length;e&&(b=Cr().getSequenceCount(e));b>=a?vr||(vr=Ir(function(){Jr({writeThenSend:!0},M("flush_only_full_queue")?c:void 0,d);vr=void 0},0)):10<=f-g&&(Kr(d),d?ur.j=f:tr.j=f)}
function Lr(a,b){M("web_all_payloads_via_jspb")&&dl(new P("transport.logIsolatedGelPayload called in JSPB only experiment"));if("log_event"===a.endpoint){Er(a);var c=Fr(a),d=new Map;d.set(c,[a.payload]);b&&(rr=new b);return new Bf(function(e,f){rr&&rr.isReady()?Mr(d,rr,e,f,{bypassNetworkless:!0},!0):e()})}}
function Nr(a,b){if("log_event"===a.endpoint){Er(void 0,a);var c=Fr(a,!0),d=new Map;d.set(c,[a.payload.toJSON()]);b&&(rr=new b);return new Bf(function(e){rr&&rr.isReady()?Or(d,rr,e,{bypassNetworkless:!0},!0):e()})}}
function Fr(a,b){var c="";if(a.dangerousLogToVisitorSession)c="visitorOnlyApprovedKey";else if(a.cttAuthInfo){if(void 0===b?0:b){b=a.cttAuthInfo.token;c=a.cttAuthInfo;var d=new jk;c.videoId?d.setVideoId(c.videoId):c.playlistId&&Wd(d,2,Ek,c.playlistId);Ar[b]=d}else b=a.cttAuthInfo,c={},b.videoId?c.videoId=b.videoId:b.playlistId&&(c.playlistId=b.playlistId),zr[a.cttAuthInfo.token]=c;c=a.cttAuthInfo.token}return c}
function Jr(a,b,c){a=void 0===a?{}:a;c=void 0===c?!1:c;!c&&M("web_all_payloads_via_jspb")&&dl(new P("transport.flushLogs called for JSON in JSPB only experiment"));new Bf(function(d,e){c?(Pr(ur.i),Pr(ur.h),ur.h=0):(Pr(tr.i),Pr(tr.h),tr.h=0);if(rr&&rr.isReady())if(M("use_new_in_memory_storage")){var f=a,g=c,h=rr;f=void 0===f?{}:f;g=void 0===g?!1:g;var l=new Map,m=new Map;if(void 0!==b)g?(e=Cr().extractMatchingEntries({isJspb:g,cttAuthInfo:b}),l.set(b,e),Or(l,h,d,f)):(l=Cr().extractMatchingEntries({isJspb:g,
cttAuthInfo:b}),m.set(b,l),Mr(m,h,d,e,f));else if(g){e=p(Object.keys(Br));for(g=e.next();!g.done;g=e.next())m=g.value,g=Cr().extractMatchingEntries({isJspb:!0,cttAuthInfo:m}),0<g.length&&l.set(m,g),delete Br[m];Or(l,h,d,f)}else{l=p(Object.keys(Br));for(g=l.next();!g.done;g=l.next()){g=g.value;var q=Cr().extractMatchingEntries({isJspb:!1,cttAuthInfo:g});0<q.length&&m.set(g,q);delete Br[g]}Mr(m,h,d,e,f)}}else f=a,l=c,h=rr,f=void 0===f?{}:f,l=void 0===l?!1:l,void 0!==b?l?(e=new Map,l=yr.get(b)||[],e.set(b,
l),Or(e,h,d,f),yr.delete(b)):(l=new Map,m=xr.get(b)||[],l.set(b,m),Mr(l,h,d,e,f),xr.delete(b)):l?(Or(yr,h,d,f),yr.clear()):(Mr(xr,h,d,e,f),xr.clear());else Kr(c),d()})}
function Kr(a){a=void 0===a?!1:a;if(M("web_gel_timeout_cap")&&(!a&&!tr.h||a&&!ur.h)){var b=Ir(function(){Jr({writeThenSend:!0},void 0,a)},pr);
a?ur.h=b:tr.h=b}Pr(a?ur.i:tr.i);b=L("LOGGING_BATCH_TIMEOUT",Uk("web_gel_debounce_ms",1E4));M("shorten_initial_gel_batch_timeout")&&wr&&(b=or);b=Ir(function(){Jr({writeThenSend:!0},void 0,a)},b);
a?ur.i=b:tr.i=b}
function Mr(a,b,c,d,e,f){e=void 0===e?{}:e;var g=Math.round(Q()),h=a.size,l={};a=p(a);for(var m=a.next();!m.done;l={Ta:l.Ta,ra:l.ra,Ea:l.Ea,Va:l.Va,Ua:l.Ua},m=a.next()){var q=p(m.value);m=q.next().value;q=q.next().value;l.ra=xb({context:so(b.config_||ro())});if(!Ra(q)&&!M("throw_err_when_logevent_malformed_killswitch")){d();break}l.ra.events=q;(q=zr[m])&&Qr(l.ra,m,q);delete zr[m];l.Ea="visitorOnlyApprovedKey"===m;Rr(l.ra,g,l.Ea);Sr(e);l.Va=function(r){M("update_log_event_config")&&fi.S(function(){return x(function(w){return v(w,
Tr(r),0)})});
h--;h||c()};
l.Ta=0;l.Ua=function(r){return function(){r.Ta++;if(e.bypassNetworkless&&1===r.Ta)try{Ho(b,"log_event",r.ra,Ur({writeThenSend:!0},r.Ea,r.Va,r.Ua,f)),wr=!1}catch(w){cl(w),d()}h--;h||c()}}(l);
try{Ho(b,"log_event",l.ra,Ur(e,l.Ea,l.Va,l.Ua,f)),wr=!1}catch(r){cl(r),d()}}}
function Or(a,b,c,d,e){d=void 0===d?{}:d;var f=Math.round(Q()),g=a.size,h=new Map([].concat(ja(a)));h=p(h);for(var l=h.next();!l.done;l=h.next()){var m=p(l.value).next().value,q=a.get(m);l=new Fk;var r=zo(b.config_||ro());G(l,lj,1,r);q=q?Vr(q):[];q=p(q);for(r=q.next();!r.done;r=q.next())de(l,3,fk,r.value);(q=Ar[m])&&Wr(l,m,q);delete Ar[m];m="visitorOnlyApprovedKey"===m;Xr(l,f,m);Sr(d);l=le(l);m=Ur(d,m,function(w){M("update_log_event_config")&&fi.S(function(){return x(function(t){return v(t,Tr(w),
0)})});
g--;g||c()},function(){g--;
g||c()},e);
m.headers["Content-Type"]="application/json+protobuf";m.postBodyFormat="JSPB";m.postBody=l;Ho(b,"log_event","",m);wr=!1}}
function Sr(a){M("always_send_and_write")&&(a.writeThenSend=!1)}
function Ur(a,b,c,d,e){a={retry:!0,onSuccess:c,onError:d,hc:a,dangerousLogToVisitorSession:b,xr:!!e,headers:{},postBodyFormat:"",postBody:""};Yr()&&(a.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(Q())));return a}
function Rr(a,b,c){Yr()||(a.requestTimeMs=String(b));M("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=L("EVENT_ID"))&&(c=Zr(),a.serializedClientEventId={serializedEventId:b,clientCounter:String(c)})}
function Xr(a,b,c){Yr()||D(a,2,b);if(!c&&(b=L("EVENT_ID"))){c=Zr();var d=new ik;D(d,1,b);D(d,2,c);G(a,ik,5,d)}}
function Zr(){var a=L("BATCH_CLIENT_COUNTER")||0;a||(a=Math.floor(Math.random()*qr/2));a++;a>qr&&(a=1);Rk("BATCH_CLIENT_COUNTER",a);return a}
function Qr(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function Wr(a,b,c){if(ee(c,1===Xd(c,Ek)?1:-1))var d=1;else if(c.getPlaylistId())d=2;else return;G(a,jk,4,c);a=Yd(a,lj,1)||new lj;c=Yd(a,jj,3)||new jj;var e=new ij;D(e,2,b);D(e,1,d);de(c,12,ij,e);G(a,jj,3,c)}
function Vr(a){for(var b=[],c=0;c<a.length;c++)try{b.push(new fk(a[c]))}catch(d){cl(new P("Transport failed to deserialize "+String(a[c])))}return b}
function Er(a,b){if(B("yt.logging.transport.enableScrapingForTest")){var c=B("yt.logging.transport.scrapedPayloadsForTesting"),d=B("yt.logging.transport.payloadToScrape","");b&&(b=B("yt.logging.transport.getScrapedPayloadFromClientEventsFunction").bind(b.payload)())&&c.push(b);a&&a.payload[d]&&c.push((null==a?void 0:a.payload)[d]);z("yt.logging.transport.scrapedPayloadsForTesting",c)}}
function Yr(){return M("use_request_time_ms_header")||M("lr_use_request_time_ms_header")}
function Ir(a,b){return M("transport_use_scheduler")?nm(a,b):tl(a,b)}
function Pr(a){M("transport_use_scheduler")?fi.ea(a):window.clearTimeout(a)}
function Tr(a){var b,c,d,e,f,g,h,l,m,q;return x(function(r){return 1==r.h?(d=null==(b=a)?void 0:null==(c=b.responseContext)?void 0:c.globalConfigGroup,e=nr(d,Vi),g=null==(f=d)?void 0:f.hotHashData,h=nr(d,Ui),m=null==(l=d)?void 0:l.coldHashData,q=ir().resolve(no),g?e?v(r,oo(q,g,e),2):v(r,oo(q,g),2):r.u(2)):m?h?v(r,po(q,m,h),0):v(r,po(q,m),0):r.u(0)})}
;var $r=y.ytLoggingGelSequenceIdObj_||{};z("ytLoggingGelSequenceIdObj_",$r);
function as(a,b,c,d){d=void 0===d?{}:d;var e={},f=Math.round(d.timestamp||Q());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;M("enable_unknown_lact_fix_on_html5")&&Nq();a=Qq();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};M("log_sequence_info_on_gel_web")&&d.sequenceGroup&&(a=e.context,b=d.sequenceGroup,b={index:bs(b),groupKey:b},a.sequence=b,d.endOfSequence&&delete $r[d.sequenceGroup]);(d.sendIsolatedPayload?Lr:Dr)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,
dangerousLogToVisitorSession:d.dangerousLogToVisitorSession},c)}
function cs(a){Jr(void 0,void 0,void 0===a?!1:a)}
function bs(a){$r[a]=a in $r?$r[a]+1:0;return $r[a]}
;var ds=[];function Em(a,b,c){c=void 0===c?{}:c;var d=zq;L("ytLoggingEventsDefaultDisabled",!1)&&zq===zq&&(d=null);M("web_all_payloads_via_jspb")?ds.push({Fb:a,payload:b,options:c}):as(a,b,d,c)}
;var es=y.ytLoggingGelSequenceIdObj_||{};z("ytLoggingGelSequenceIdObj_",es);
function fs(a,b,c){c=void 0===c?{}:c;var d=Math.round(c.timestamp||Q());D(a,1,d<Number.MAX_SAFE_INTEGER?d:0);var e=Qq();d=new ek;D(d,1,c.timestamp||!isFinite(e)?-1:e);if(M("log_sequence_info_on_gel_web")&&c.sequenceGroup){e=c.sequenceGroup;var f=bs(e),g=new dk;D(g,2,f);D(g,1,e);G(d,dk,3,g);c.endOfSequence&&delete es[c.sequenceGroup]}G(a,ek,33,d);(c.sendIsolatedPayload?Nr:Hr)({endpoint:"log_event",payload:a,cttAuthInfo:c.cttAuthInfo,dangerousLogToVisitorSession:c.dangerousLogToVisitorSession},b)}
;function gs(a,b){b=void 0===b?{}:b;var c=!1;L("ytLoggingEventsDefaultDisabled",!1)&&(c=!0);fs(a,c?null:zq,b)}
;function hs(a,b,c){var d=new fk;be(d,Uj,72,gk,a);c?fs(d,c,b):gs(d,b)}
function is(a,b,c){var d=new fk;be(d,Tj,73,gk,a);c?fs(d,c,b):gs(d,b)}
function js(a,b,c){var d=new fk;be(d,Sj,78,gk,a);c?fs(d,c,b):gs(d,b)}
function ks(a,b,c){var d=new fk;be(d,Vj,208,gk,a);c?fs(d,c,b):gs(d,b)}
function ls(a,b,c){var d=new fk;be(d,Lj,156,gk,a);c?fs(d,c,b):gs(d,b)}
function ms(a,b,c){var d=new fk;be(d,Pj,215,gk,a);c?fs(d,c,b):gs(d,b)}
;var ns=new Set,os=0,ps=0,qs=0,rs=[],ss=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function Dm(a){ts(a)}
function us(a){ts(a,"WARNING")}
function ts(a,b,c,d,e,f){f=void 0===f?{}:f;f.name=c||L("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||L("INNERTUBE_CONTEXT_CLIENT_VERSION");var g=f||{},h=void 0===b?"ERROR":b;h=void 0===h?"ERROR":h;if(a){a.hasOwnProperty("level")&&a.level&&(h=a.level);if(M("console_log_js_exceptions")){var l=[];l.push("Name: "+a.name);l.push("Message: "+a.message);a.hasOwnProperty("params")&&l.push("Error Params: "+JSON.stringify(a.params));a.hasOwnProperty("args")&&l.push("Error args: "+JSON.stringify(a.args));
l.push("File name: "+a.fileName);l.push("Stacktrace: "+a.stack);window.console.log(l.join("\n"),a)}if(!(5<=os)){var m=rs,q=ye(a),r=q.message||"Unknown Error",w=q.name||"UnknownError",t=q.stack||a.i||"Not available";if(t.startsWith(w+": "+r)){var A=t.split("\n");A.shift();t=A.join("\n")}var E=q.lineNumber||"Not available",F=q.fileName||"Not available",O=t,N=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var R=0;R<a.args.length&&!(N=Sl(a.args[R],"params."+R,g,N),500<=N);R++);else if(a.hasOwnProperty("params")&&
a.params){var ca=a.params;if("object"===typeof a.params)for(var U in ca){if(ca[U]){var rb="params."+U,Wa=Ul(ca[U]);g[rb]=Wa;N+=rb.length+Wa.length;if(500<N)break}}else g.params=Ul(ca)}if(m.length)for(var oa=0;oa<m.length&&!(N=Sl(m[oa],"params.context."+oa,g,N),500<=N);oa++);navigator.vendor&&!g.hasOwnProperty("vendor")&&(g["device.vendor"]=navigator.vendor);var I={message:r,name:w,lineNumber:E,fileName:F,stack:O,params:g,sampleWeight:1},ma=Number(a.columnNumber);isNaN(ma)||(I.lineNumber=I.lineNumber+
":"+ma);if("IGNORED"===a.level)var ea=0;else a:{for(var He=Ol(),Ie=p(He.na),td=Ie.next();!td.done;td=Ie.next()){var ra=td.value;if(I.message&&I.message.match(ra.Ir)){ea=ra.weight;break a}}for(var Ap=p(He.la),kk=Ap.next();!kk.done;kk=Ap.next()){var Bp=kk.value;if(Bp.callback(I)){ea=Bp.weight;break a}}ea=1}I.sampleWeight=ea;for(var Cp=p(Jl),lk=Cp.next();!lk.done;lk=Cp.next()){var mk=lk.value;if(mk.kb[I.name])for(var Dp=p(mk.kb[I.name]),nk=Dp.next();!nk.done;nk=Dp.next()){var Ep=nk.value,Xg=I.message.match(Ep.regexp);
if(Xg){I.params["params.error.original"]=Xg[0];for(var ok=Ep.groups,Fp={},ud=0;ud<ok.length;ud++)Fp[ok[ud]]=Xg[ud+1],I.params["params.error."+ok[ud]]=Xg[ud+1];I.message=mk.Cb(Fp);break}}}I.params||(I.params={});var Gp=Ol();I.params["params.errorServiceSignature"]="msg="+Gp.na.length+"&cb="+Gp.la.length;I.params["params.serviceWorker"]="false";y.document&&y.document.querySelectorAll&&(I.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));Eb("sample").constructor!==
Cb&&(I.params["params.fconst"]="true");window.yterr&&"function"===typeof window.yterr&&window.yterr(I);if(0!==I.sampleWeight&&!ns.has(I.message)){if("ERROR"===h){Pl.sa("handleError",I);if(M("record_app_crashed_web")&&0===qs&&1===I.sampleWeight)if(qs++,M("errors_via_jspb")){var pk=new Ej;D(pk,1,1);if(!M("report_client_error_with_app_crash_ks")){var Hp=new zj;D(Hp,1,I.message);var Ip=new Aj;G(Ip,zj,3,Hp);var Jp=new Bj;G(Jp,Aj,5,Ip);var Kp=new Cj;G(Kp,Bj,9,Jp);G(pk,Cj,4,Kp)}var Lp=new fk;be(Lp,Ej,20,
gk,pk);gs(Lp)}else{var Mp={appCrashType:"APP_CRASH_TYPE_BREAKPAD"};M("report_client_error_with_app_crash_ks")||(Mp.systemHealth={crashData:{clientError:{logMessage:{message:I.message}}}});Em("appCrashed",Mp)}ps++}else"WARNING"===h&&Pl.sa("handleWarning",I);if(M("kevlar_gel_error_routing"))a:{var Je=h;if(M("errors_via_jspb")){if(vs())var Op=void 0;else{var vd=new wj;D(vd,1,I.stack);I.fileName&&D(vd,4,I.fileName);var Jb=I.lineNumber&&I.lineNumber.split?I.lineNumber.split(":"):[];0!==Jb.length&&(1!==
Jb.length||isNaN(Number(Jb[0]))?2!==Jb.length||isNaN(Number(Jb[0]))||isNaN(Number(Jb[1]))||(D(vd,2,Number(Jb[0])),D(vd,3,Number(Jb[1]))):D(vd,2,Number(Jb[0])));var zc=new zj;D(zc,1,I.message);D(zc,3,I.name);D(zc,6,I.sampleWeight);"ERROR"===Je?D(zc,2,2):"WARNING"===Je?D(zc,2,1):D(zc,2,0);var qk=new xj;D(qk,1,!0);be(qk,wj,3,yj,vd);var $b=new tj;D($b,3,window.location.href);for(var Pp=L("FEXP_EXPERIMENTS",[]),rk=0;rk<Pp.length;rk++){var ow=Pp[rk];Gd($b);Vd($b,5,2,!1,!1).push(ow)}var sk=L("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");
if(!Sk()&&sk)for(var Qp=p(Object.keys(sk)),Ac=Qp.next();!Ac.done;Ac=Qp.next()){var Rp=Ac.value,tk=new vj;D(tk,1,Rp);D(tk,2,String(sk[Rp]));de($b,4,vj,tk)}var uk=I.params;if(uk){var Sp=p(Object.keys(uk));for(Ac=Sp.next();!Ac.done;Ac=Sp.next()){var Tp=Ac.value,vk=new vj;D(vk,1,"client."+Tp);D(vk,2,String(uk[Tp]));de($b,4,vj,vk)}}var Up=L("SERVER_NAME"),Vp=L("SERVER_VERSION");if(Up&&Vp){var wk=new vj;D(wk,1,"server.name");D(wk,2,Up);de($b,4,vj,wk);var xk=new vj;D(xk,1,"server.version");D(xk,2,Vp);de($b,
4,vj,xk)}var Yg=new Aj;G(Yg,tj,1,$b);G(Yg,xj,2,qk);G(Yg,zj,3,zc);Op=Yg}var Wp=Op;if(!Wp)break a;var Xp=new fk;be(Xp,Aj,163,gk,Wp);gs(Xp)}else{if(vs())var Yp=void 0;else{var Ke={stackTrace:I.stack};I.fileName&&(Ke.filename=I.fileName);var Kb=I.lineNumber&&I.lineNumber.split?I.lineNumber.split(":"):[];0!==Kb.length&&(1!==Kb.length||isNaN(Number(Kb[0]))?2!==Kb.length||isNaN(Number(Kb[0]))||isNaN(Number(Kb[1]))||(Ke.lineNumber=Number(Kb[0]),Ke.columnNumber=Number(Kb[1])):Ke.lineNumber=Number(Kb[0]));
var yk={level:"ERROR_LEVEL_UNKNOWN",message:I.message,errorClassName:I.name,sampleWeight:I.sampleWeight};"ERROR"===Je?yk.level="ERROR_LEVEL_ERROR":"WARNING"===Je&&(yk.level="ERROR_LEVEL_WARNNING");var pw={isObfuscated:!0,browserStackInfo:Ke},wd={pageUrl:window.location.href,kvPairs:[]};L("FEXP_EXPERIMENTS")&&(wd.experimentIds=L("FEXP_EXPERIMENTS"));var zk=L("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");if(!Sk()&&zk)for(var Zp=p(Object.keys(zk)),Bc=Zp.next();!Bc.done;Bc=Zp.next()){var $p=Bc.value;wd.kvPairs.push({key:$p,
value:String(zk[$p])})}var Ak=I.params;if(Ak){var aq=p(Object.keys(Ak));for(Bc=aq.next();!Bc.done;Bc=aq.next()){var bq=Bc.value;wd.kvPairs.push({key:"client."+bq,value:String(Ak[bq])})}}var cq=L("SERVER_NAME"),dq=L("SERVER_VERSION");cq&&dq&&(wd.kvPairs.push({key:"server.name",value:cq}),wd.kvPairs.push({key:"server.version",value:dq}));Yp={errorMetadata:wd,stackTrace:pw,logMessage:yk}}var eq=Yp;if(!eq)break a;Em("clientError",eq)}if("ERROR"===Je||M("errors_flush_gel_always_killswitch"))b:{if(M("web_fp_via_jspb")&&
(cs(!0),!M("web_fp_via_jspb_and_json")))break b;cs()}}if(!M("suppress_error_204_logging")){var Le=I.params||{},ac={urlParams:{a:"logerror",t:"jserror",type:I.name,msg:I.message.substr(0,250),line:I.lineNumber,level:h,"client.name":Le.name},postParams:{url:L("PAGE_NAME",window.location.href),file:I.fileName},method:"POST"};Le.version&&(ac["client.version"]=Le.version);if(ac.postParams){I.stack&&(ac.postParams.stack=I.stack);for(var fq=p(Object.keys(Le)),Bk=fq.next();!Bk.done;Bk=fq.next()){var gq=Bk.value;
ac.postParams["client."+gq]=Le[gq]}var Ck=L("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");if(Ck)for(var hq=p(Object.keys(Ck)),Dk=hq.next();!Dk.done;Dk=hq.next()){var iq=Dk.value;ac.postParams[iq]=Ck[iq]}var jq=L("SERVER_NAME"),kq=L("SERVER_VERSION");jq&&kq&&(ac.postParams["server.name"]=jq,ac.postParams["server.version"]=kq)}zl(L("ECATCHER_REPORT_HOST","")+"/error_204",ac)}try{ns.add(I.message)}catch(Rx){}os++}}}}
function vs(){for(var a=p(ss),b=a.next();!b.done;b=a.next())if(Il(b.value.toLowerCase()))return!0;return!1}
function ws(a){var b=Ka.apply(1,arguments);a.args||(a.args=[]);a.args.push.apply(a.args,ja(b))}
;function xs(){this.register=new Map}
function ys(a){a=p(a.register.values());for(var b=a.next();!b.done;b=a.next())b.value.Mr("ABORTED")}
xs.prototype.clear=function(){ys(this);this.register.clear()};
var zs=new xs;var As=Date.now().toString();
function Bs(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;16>a;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(256*Math.random())}if(As)for(a=1,b=0;b<As.length;b++)d[a%16]=d[a%16]^d[(a-1)%16]/4^As.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var Cs=y.ytLoggingDocDocumentNonce_;Cs||(Cs=Bs(),z("ytLoggingDocDocumentNonce_",Cs));var Ds=Cs;var Es={fi:0,ye:1,Ie:2,em:3,hi:4,Iq:5,Um:6,Mo:7,bo:8,Ao:9,0:"DEFAULT",1:"CHAT",2:"CONVERSATIONS",3:"MINIPLAYER",4:"DIALOG",5:"VOZ",6:"MUSIC_WATCH_TABS",7:"SHARE",8:"PUSH_NOTIFICATIONS",9:"RICH_GRID_WATCH"};function Fs(a){this.G=a}
function Gs(a){return new Fs({trackingParams:a})}
Fs.prototype.getAsJson=function(){var a={};void 0!==this.G.trackingParams?a.trackingParams=this.G.trackingParams:(a.veType=this.G.veType,void 0!==this.G.veCounter&&(a.veCounter=this.G.veCounter),void 0!==this.G.elementIndex&&(a.elementIndex=this.G.elementIndex));void 0!==this.G.dataElement&&(a.dataElement=this.G.dataElement.getAsJson());void 0!==this.G.youtubeData&&(a.youtubeData=this.G.youtubeData);return a};
Fs.prototype.getAsJspb=function(){var a=new Gj;if(void 0!==this.G.trackingParams){var b=this.G.trackingParams;if(null!=b)if("string"===typeof b)b=b?new ld(b,id):md();else if(b.constructor!==ld)if(hd(b))b=b.length?new ld(new Uint8Array(b),id):md();else throw Error();D(a,1,b)}else void 0!==this.G.veType&&D(a,2,this.G.veType),void 0!==this.G.veCounter&&D(a,6,this.G.veCounter),void 0!==this.G.elementIndex&&D(a,3,this.G.elementIndex);void 0!==this.G.dataElement&&(b=this.G.dataElement.getAsJspb(),G(a,Gj,
7,b));void 0!==this.G.youtubeData&&G(a,Wi,8,this.G.jspbYoutubeData);return a};
Fs.prototype.toString=function(){return JSON.stringify(this.getAsJson())};
Fs.prototype.isClientVe=function(){return!this.G.trackingParams&&!!this.G.veType};function Hs(a){a=void 0===a?0:a;return 0===a?"client-screen-nonce":"client-screen-nonce."+a}
function Is(a){a=void 0===a?0:a;return 0===a?"ROOT_VE_TYPE":"ROOT_VE_TYPE."+a}
function Js(a){return L(Is(void 0===a?0:a))}
z("yt_logging_screen.getRootVeType",Js);function Ks(a){return(a=Js(void 0===a?0:a))?new Fs({veType:a,youtubeData:void 0,jspbYoutubeData:void 0}):null}
function Ls(){var a=L("csn-to-ctt-auth-info");a||(a={},Rk("csn-to-ctt-auth-info",a));return a}
function Ms(a){a=L(Hs(void 0===a?0:a));if(!a&&!L("USE_CSN_FALLBACK",!0))return null;a||(a="UNDEFINED_CSN");return a?a:null}
z("yt_logging_screen.getCurrentCsn",Ms);function Ns(a,b,c){var d=Ls();(c=Ms(c))&&delete d[c];b&&(d[a]=b)}
function Os(a){return Ls()[a]}
z("yt_logging_screen.getCttAuthInfo",Os);function Ps(a,b,c,d){c=void 0===c?0:c;if(a!==L(Hs(c))||b!==L(Is(c)))if(Ns(a,d,c),Rk(Hs(c),a),Rk(Is(c),b),b=function(){setTimeout(function(){if(a)if(M("web_time_via_jspb")){var e=new Hj;D(e,1,Ds);D(e,2,a);var f=new fk;be(f,Hj,111,gk,e);gs(f)}else Em("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:Ds,clientScreenNonce:a})},0)},"requestAnimationFrame"in window)try{window.requestAnimationFrame(b)}catch(e){b()}else b()}
z("yt_logging_screen.setCurrentScreen",Ps);var Qs=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};z("yt.msgs_",Qs);function Rs(a){Mk(Qs,arguments)}
;var Ss={xe:3611,Cd:27686,Dd:85013,Ed:23462,Gd:157557,Hd:42016,Id:62407,Jd:26926,Fd:43781,Kd:51236,Ld:79148,Md:50160,Nd:77504,Zd:153587,ae:87907,be:18630,ce:54445,de:80935,ee:152172,ge:105675,he:150723,ie:37521,je:147285,ke:47786,le:98349,me:168271,ne:168954,oe:168277,pe:168273,qe:168270,re:123695,se:6827,te:29434,ue:7282,we:124448,Ae:32276,ze:76278,Be:147868,Ce:147869,De:93911,Ee:106531,Fe:27259,Ge:27262,He:27263,Je:21759,Ke:27107,Le:62936,Me:160866,Ne:49568,Oe:160789,Pe:38408,Qe:80637,Re:68727,Se:68728,
Te:80353,Ue:80356,Ve:74610,We:45707,Xe:83962,Ye:83970,Ze:46713,af:89711,bf:74612,cf:155792,df:93265,ef:74611,ff:131380,hf:128979,jf:139311,kf:128978,gf:131391,lf:105350,nf:139312,pf:134800,mf:131392,rf:113533,sf:93252,tf:99357,vf:94521,wf:114252,xf:113532,yf:94522,uf:94583,zf:88E3,Af:139580,Bf:93253,Cf:93254,Df:94387,Ef:94388,Ff:93255,Gf:97424,qf:72502,Hf:110111,If:76019,Kf:117092,Lf:117093,Jf:89431,Mf:110466,Nf:77240,Of:60508,Pf:148123,Qf:148124,Rf:137401,Sf:137402,Tf:137046,Uf:73393,Vf:113534,Wf:92098,
Xf:131381,Yf:84517,Zf:83759,ag:162711,cg:162712,dg:80357,eg:86113,fg:72598,gg:168413,hg:72733,ig:107349,jg:124275,kg:118203,lg:133275,mg:160157,ng:152569,og:156651,pg:133274,qg:160159,rg:160158,sg:133272,tg:133273,ug:133276,vg:144507,wg:143247,xg:156652,yg:143248,zg:143249,Ag:143250,Bg:143251,Cg:156653,Dg:144401,Fg:117431,Eg:133797,Gg:153964,Hg:128572,Ig:133405,Jg:117429,Kg:117430,Lg:117432,Mg:120080,Ng:117259,Og:156655,Pg:156654,Qg:121692,Rg:145656,Sg:156656,Tg:145655,Ug:145653,Vg:145654,Wg:145657,
Xg:132972,Yg:133051,Zg:133658,ah:132971,bh:97615,eh:143359,dh:143356,gh:143361,fh:143358,ih:143360,hh:143357,jh:142303,kh:143353,lh:143354,mh:144479,nh:143355,oh:31402,qh:133624,rh:146477,sh:133623,th:133622,ph:133621,uh:84774,wh:160801,vh:95117,xh:150497,yh:98930,zh:98931,Ah:98932,Bh:153320,Ch:153321,Dh:43347,Eh:129889,Fh:149123,Gh:45474,Hh:100352,Ih:84758,Jh:98443,Kh:117985,Lh:74613,Mh:155911,Nh:74614,Oh:64502,Ph:136032,Qh:74615,Rh:74616,Sh:122224,Th:74617,Uh:77820,Vh:74618,Wh:93278,Xh:93274,Yh:93275,
Zh:93276,ai:22110,bi:29433,ci:133798,di:132295,gi:120541,ii:82047,ji:113550,ki:75836,li:75837,mi:42352,ni:84512,oi:76065,ri:75989,xi:51879,yi:16623,zi:32594,Ai:27240,Bi:32633,Ci:74858,Di:156999,Fi:3945,Ei:16989,Gi:45520,Hi:25488,Ii:25492,Ji:25494,Ki:55760,Li:14057,Mi:18451,Ni:57204,Oi:57203,Pi:17897,Qi:57205,Ri:18198,Si:17898,Ti:17909,Ui:43980,Vi:46220,Wi:11721,Xi:147994,Yi:49954,Zi:96369,aj:3854,bj:151633,cj:56251,dj:159108,ej:25624,fj:152036,wj:16906,xj:99999,yj:68172,zj:27068,Aj:47973,Bj:72773,
Cj:26970,Dj:26971,Ej:96805,Fj:17752,Gj:73233,Hj:109512,Ij:22256,Jj:14115,Kj:22696,Lj:89278,Mj:89277,Nj:109513,Oj:43278,Pj:43459,Qj:43464,Rj:89279,Sj:43717,Tj:55764,Uj:22255,Vj:147912,Wj:89281,Xj:40963,Yj:43277,Zj:167701,ak:43442,bk:91824,ck:120137,dk:96367,ek:36850,fk:72694,gk:37414,hk:36851,jk:124863,ik:121343,kk:73491,lk:54473,mk:166861,nk:43375,pk:46674,qk:143815,rk:139095,sk:144402,tk:149968,uk:149969,vk:32473,wk:72901,xk:72906,yk:50947,zk:50612,Ak:50613,Bk:50942,Ck:84938,Dk:84943,Ek:84939,Fk:84941,
Gk:84944,Hk:84940,Ik:84942,Jk:35585,Kk:51926,Lk:79983,Mk:63238,Nk:18921,Ok:63241,Pk:57893,Qk:41182,Rk:135732,Sk:33424,Tk:22207,Uk:42993,Vk:36229,Wk:22206,Xk:22205,Yk:18993,Zk:19001,al:18990,bl:18991,dl:18997,fl:18725,il:19003,jl:36874,kl:44763,ll:33427,ml:67793,nl:22182,ol:37091,pl:34650,ql:50617,rl:47261,sl:22287,ul:25144,vl:97917,wl:62397,xl:150871,yl:150874,zl:125598,Al:137935,Bl:36961,Cl:108035,Dl:27426,El:27857,Fl:27846,Gl:27854,Hl:69692,Il:61411,Jl:39299,Kl:38696,Ll:62520,Ml:36382,Nl:108701,
Ol:50663,Pl:36387,Ql:14908,Rl:37533,Sl:105443,Tl:61635,Ul:62274,Vl:161670,Wl:133818,Xl:65702,Yl:65703,Zl:65701,am:76256,bm:166382,cm:37671,dm:49953,fm:36216,gm:28237,hm:39553,im:29222,jm:26107,km:38050,lm:26108,nm:120745,mm:26109,om:26110,pm:66881,qm:28236,rm:14586,sm:160598,tm:57929,um:74723,vm:44098,wm:44099,zm:23528,Am:61699,xm:134104,ym:134103,Bm:59149,Cm:101951,Dm:97346,Em:118051,Fm:95102,Gm:64882,Hm:119505,Im:63595,Jm:63349,Km:95101,Lm:75240,Mm:27039,Nm:68823,Om:21537,Pm:83464,Qm:75707,Rm:83113,
Sm:101952,Tm:101953,Vm:79610,Wm:125755,Xm:24402,Ym:24400,Zm:32925,bn:57173,an:156421,cn:122502,dn:145268,en:138480,fn:64423,gn:64424,hn:33986,jn:100828,kn:129089,ln:21409,qn:135155,rn:135156,sn:135157,tn:135158,un:158225,vn:135159,wn:135160,xn:167651,yn:135161,An:135162,Bn:135163,zn:158226,Cn:158227,Dn:135164,En:135165,Fn:135166,mn:11070,nn:11074,pn:17880,Gn:14001,In:30709,Jn:30707,Kn:30711,Ln:30710,Mn:30708,Hn:26984,Nn:146143,On:63648,Pn:63649,Qn:111059,Rn:5754,Sn:20445,Tn:151308,Un:151152,Xn:130975,
Wn:130976,Vn:167637,Yn:110386,Zn:113746,ao:66557,co:17310,eo:28631,fo:21589,ho:164817,jo:168011,ko:154946,lo:68012,mo:162617,no:60480,oo:138664,po:141121,qo:164502,ro:31571,so:141978,to:150105,uo:150106,vo:150107,wo:150108,xo:76980,yo:41577,zo:45469,Bo:38669,Co:13768,Do:13777,Eo:141842,Fo:62985,Go:4724,Ho:59369,Io:43927,Jo:43928,Ko:12924,Lo:100355,Oo:56219,Po:27669,Qo:10337,No:47896,Ro:122629,To:139723,So:139722,Uo:121258,Vo:107598,Wo:127991,Xo:96639,Yo:107536,Zo:130169,ap:96661,bp:145188,cp:96658,
ep:116646,fp:159428,gp:121122,hp:96660,ip:127738,jp:127083,kp:155281,lp:162959,mp:163566,np:147842,qp:104443,rp:96659,sp:147595,tp:106442,up:162776,vp:134840,wp:63667,xp:63668,yp:63669,zp:130686,Ap:147036,Bp:78314,Cp:147799,Dp:148649,Ep:55761,Fp:127098,Gp:134841,Hp:96368,Ip:67374,Jp:48992,Kp:146176,Lp:49956,Mp:31961,Np:26388,Op:23811,Pp:5E4,Qp:126250,Rp:96370,Sp:47355,Tp:47356,Up:37935,Vp:45521,Wp:21760,Xp:83769,Yp:49977,Zp:49974,aq:93497,bq:93498,cq:34325,fq:140759,gq:115803,hq:123707,iq:100081,
jq:35309,kq:68314,lq:25602,mq:100339,nq:143516,oq:59018,pq:18248,qq:50625,rq:9729,sq:37168,tq:37169,uq:21667,wq:16749,xq:18635,yq:39305,zq:18046,Aq:53969,Bq:8213,Cq:93926,Dq:102852,Eq:110099,Fq:22678,Gq:69076,Hq:137575,Jq:139224,Kq:100856,Lq:154430,Mq:17736,Nq:3832,Oq:147111,Pq:55759,Qq:64031,Wq:93044,Xq:93045,Zq:34388,Yq:167841,br:17657,dr:17655,er:39579,fr:39578,gr:77448,hr:8196,ir:11357,jr:69877,kr:8197,lr:168501,mr:156512,pr:161613,qr:156509,rr:161612,sr:161614,tr:82039};function Ts(){var a=wb(Us),b;return(new Bf(function(c,d){a.onSuccess=function(e){sl(e)?c(new Vs(e)):d(new Ws("Request failed, status="+(e&&"status"in e?e.status:-1),"net.badstatus",e))};
a.onError=function(e){d(new Ws("Unknown request error","net.unknown",e))};
a.onTimeout=function(e){d(new Ws("Request timed out","net.timeout",e))};
b=zl("//googleads.g.doubleclick.net/pagead/id",a)})).qb(function(c){c instanceof If&&b.abort();
return Gf(c)})}
function Ws(a,b,c){cb.call(this,a+", errorCode="+b);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}
u(Ws,cb);function Vs(a){this.xhr=a}
;function Xs(){this.h=0;this.ba=null}
Xs.prototype.then=function(a,b,c){return 1===this.h&&a?(a=a.call(c,this.ba))&&"function"===typeof a.then?a:Ys(a):2===this.h&&b?(a=b.call(c,this.ba))&&"function"===typeof a.then?a:Zs(a):this};
Xs.prototype.getValue=function(){return this.ba};
Xs.prototype.$goog_Thenable=!0;function Zs(a){var b=new Xs;a=void 0===a?null:a;b.h=2;b.ba=void 0===a?null:a;return b}
function Ys(a){var b=new Xs;a=void 0===a?null:a;b.h=1;b.ba=void 0===a?null:a;return b}
;function $s(a,b){var c=void 0===c?{}:c;a={method:void 0===b?"POST":b,mode:nl(a)?"same-origin":"cors",credentials:nl(a)?"same-origin":"include"};b={};for(var d=p(Object.keys(c)),e=d.next();!e.done;e=d.next())e=e.value,c[e]&&(b[e]=c[e]);0<Object.keys(b).length&&(a.headers=b);return a}
;function at(){return wg()||Hl&&Il("applewebkit")&&!Il("version")&&(!Il("safari")||Il("gsa/"))||Oc&&Il("version/")?!0:L("EOM_VISITOR_DATA")?!1:!0}
;function bt(a){a:{var b=a.raw_embedded_player_response;if(!b&&(a=a.embedded_player_response))try{b=JSON.parse(a)}catch(d){b="EMBEDDED_PLAYER_MODE_UNKNOWN";break a}if(b)b:{for(var c in qj)if(qj[c]==b.embeddedPlayerMode){b=qj[c];break b}b="EMBEDDED_PLAYER_MODE_UNKNOWN"}else b="EMBEDDED_PLAYER_MODE_UNKNOWN"}return"EMBEDDED_PLAYER_MODE_PFL"===b}
;function ct(a){cb.call(this,a.message||a.description||a.name);this.isMissing=a instanceof dt;this.isTimeout=a instanceof Ws&&"net.timeout"==a.errorCode;this.isCanceled=a instanceof If}
u(ct,cb);ct.prototype.name="BiscottiError";function dt(){cb.call(this,"Biscotti ID is missing from server")}
u(dt,cb);dt.prototype.name="BiscottiMissingError";var Us={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},et=null;function ft(){if(M("disable_biscotti_fetch_entirely_for_all_web_clients"))return Error("Biscotti id fetching has been disabled entirely.");if(!at())return Error("User has not consented - not fetching biscotti id.");var a=L("PLAYER_VARS",{});if("1"==ub(a))return Error("Biscotti ID is not available in private embed mode");if(bt(a))return Error("Biscotti id fetching has been disabled for pfl.")}
function Yk(){var a=ft();if(void 0!==a)return Gf(a);et||(et=Ts().then(gt).qb(function(b){return ht(2,b)}));
return et}
function gt(a){a=a.xhr.responseText;if(0!=a.lastIndexOf(")]}'",0))throw new dt;a=JSON.parse(a.substr(4));if(1<(a.type||1))throw new dt;a=a.id;Zk(a);et=Ys(a);jt(18E5,2);return a}
function ht(a,b){b=new ct(b);Zk("");et=Zs(b);0<a&&jt(12E4,a-1);throw b;}
function jt(a,b){tl(function(){Ts().then(gt,function(c){return ht(b,c)}).qb(eb)},a)}
function kt(){try{var a=B("yt.ads.biscotti.getId_");return a?a():Yk()}catch(b){return Gf(b)}}
;function lt(a){if("1"!=ub(L("PLAYER_VARS",{}))){a&&Xk();try{kt().then(function(){},function(){}),tl(lt,18E5)}catch(b){cl(b)}}}
;function mt(){var a=am.getInstance(),b=dm(119),c=1<window.devicePixelRatio;if(document.body&&pi(document.body,"exp-invert-logo"))if(c&&!pi(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!pi(d,"inverted-hdpi")){var e=ni(d);oi(d,e+(0<e.length?" inverted-hdpi":"inverted-hdpi"))}}else!c&&pi(document.body,"inverted-hdpi")&&qi();if(b!=c){b="f"+(Math.floor(119/31)+1);d=em(b)||0;d=c?d|67108864:d&-67108865;0==d?delete $l[b]:(c=d.toString(16),$l[b]=
c.toString());c=!0;M("web_secure_pref_cookie_killswitch")&&(c=!1);b=a.h;d=[];for(var f in $l)d.push(f+"="+encodeURIComponent(String($l[f])));Xl(b,d.join("&"),63072E3,a.i,c)}}
;function nt(){this.vd=!0}
function ot(a){var b={},c=yg([]);c&&(b.Authorization=c,c=a=null==a?void 0:a.sessionIndex,void 0===c&&(c=Number(L("SESSION_INDEX",0)),c=isNaN(c)?0:c),M("voice_search_auth_header_removal")||(b["X-Goog-AuthUser"]=c.toString()),"INNERTUBE_HOST_OVERRIDE"in Qk||(b["X-Origin"]=window.location.origin),void 0===a&&"DELEGATED_SESSION_ID"in Qk&&(b["X-Goog-PageId"]=L("DELEGATED_SESSION_ID")));return b}
;var pt={identityType:"UNAUTHENTICATED_IDENTITY_TYPE_UNKNOWN"};var qt=new Map([["dark","USER_INTERFACE_THEME_DARK"],["light","USER_INTERFACE_THEME_LIGHT"]]);function rt(){var a=void 0===a?window.location.href:a;if(M("kevlar_disable_theme_param"))return null;nc(oc(5,a));try{var b=ll(a).theme;return qt.get(b)||null}catch(c){}return null}
;function st(){this.h={};if(this.i=Zl()){var a=ug.get("CONSISTENCY",void 0);a&&tt(this,{encryptedTokenJarContents:a})}}
st.prototype.handleResponse=function(a,b){if(!b)throw Error("request needs to be passed into ConsistencyService");var c,d;b=(null==(c=b.ha.context)?void 0:null==(d=c.request)?void 0:d.consistencyTokenJars)||[];var e;if(a=null==(e=a.responseContext)?void 0:e.consistencyTokenJar){e=p(b);for(c=e.next();!c.done;c=e.next())delete this.h[c.value.encryptedTokenJarContents];tt(this,a)}};
function tt(a,b){if(b.encryptedTokenJarContents&&(a.h[b.encryptedTokenJarContents]=b,"string"===typeof b.expirationSeconds)){var c=Number(b.expirationSeconds);setTimeout(function(){delete a.h[b.encryptedTokenJarContents]},1E3*c);
a.i&&Xl("CONSISTENCY",b.encryptedTokenJarContents,c,void 0,!0)}}
;var ut=window.location.hostname.split(".").slice(-2).join(".");function vt(){var a=L("LOCATION_PLAYABILITY_TOKEN");"TVHTML5"===L("INNERTUBE_CLIENT_NAME")&&(this.h=wt(this))&&(a=this.h.get("yt-location-playability-token"));a&&(this.locationPlayabilityToken=a,this.i=void 0)}
var xt;vt.getInstance=function(){xt=B("yt.clientLocationService.instance");xt||(xt=new vt,z("yt.clientLocationService.instance",xt));return xt};
k=vt.prototype;k.setLocationOnInnerTubeContext=function(a){a.client||(a.client={});this.i?(a.client.locationInfo||(a.client.locationInfo={}),a.client.locationInfo.latitudeE7=Math.floor(1E7*this.i.coords.latitude),a.client.locationInfo.longitudeE7=Math.floor(1E7*this.i.coords.longitude),a.client.locationInfo.horizontalAccuracyMeters=Math.round(this.i.coords.accuracy),a.client.locationInfo.forceLocationPlayabilityTokenRefresh=!0):this.locationPlayabilityToken&&(a.client.locationPlayabilityToken=this.locationPlayabilityToken)};
k.handleResponse=function(a){var b;a=null==(b=a.responseContext)?void 0:b.locationPlayabilityToken;void 0!==a&&(this.locationPlayabilityToken=a,this.i=void 0,"TVHTML5"===L("INNERTUBE_CLIENT_NAME")?(this.h=wt(this))&&this.h.set("yt-location-playability-token",a,15552E3):Xl("YT_CL",JSON.stringify({loctok:a}),15552E3,ut,!0))};
function wt(a){return void 0===a.h?new vm("yt-client-location"):a.h}
k.clearLocationPlayabilityToken=function(a){"TVHTML5"===a?(this.h=wt(this))&&this.h.remove("yt-location-playability-token"):Yl("YT_CL")};
k.getCurrentPositionFromGeolocation=function(){var a=this;if(!(navigator&&navigator.geolocation&&navigator.geolocation.getCurrentPosition))return Promise.reject(Error("Geolocation unsupported"));var b=!1,c=1E4;"MWEB"===L("INNERTUBE_CLIENT_NAME")&&(b=!0,c=15E3);return new Promise(function(d,e){navigator.geolocation.getCurrentPosition(function(f){a.i=f;d(f)},function(f){e(f)},{enableHighAccuracy:b,
maximumAge:0,timeout:c})})};
k.createUnpluggedLocationInfo=function(a){var b={};a=a.coords;if(null==a?0:a.latitude)b.latitudeE7=Math.floor(1E7*a.latitude);if(null==a?0:a.longitude)b.longitudeE7=Math.floor(1E7*a.longitude);if(null==a?0:a.accuracy)b.locationRadiusMeters=Math.round(a.accuracy);return b};function zt(a,b){var c,d=null==(c=nr(a,pj))?void 0:c.signal;if(d&&b.Pa&&(c=b.Pa[d]))return c();var e;if((c=null==(e=nr(a,nj))?void 0:e.request)&&b.Kc&&(e=b.Kc[c]))return e();for(var f in a)if(b.Ub[f]&&(a=b.Ub[f]))return a()}
;function At(a){return function(){return new a}}
;var Bt={},Ct=(Bt.WEB_UNPLUGGED="^unplugged/",Bt.WEB_UNPLUGGED_ONBOARDING="^unplugged/",Bt.WEB_UNPLUGGED_OPS="^unplugged/",Bt.WEB_UNPLUGGED_PUBLIC="^unplugged/",Bt.WEB_CREATOR="^creator/",Bt.WEB_KIDS="^kids/",Bt.WEB_EXPERIMENTS="^experiments/",Bt.WEB_MUSIC="^music/",Bt.WEB_REMIX="^music/",Bt.WEB_MUSIC_EMBEDDED_PLAYER="^music/",Bt.WEB_MUSIC_EMBEDDED_PLAYER="^main_app/|^sfv/",Bt);
function Dt(a){var b=void 0===b?"UNKNOWN_INTERFACE":b;if(1===a.length)return a[0];var c=Ct[b];if(c){var d=new RegExp(c),e=p(a);for(c=e.next();!c.done;c=e.next())if(c=c.value,d.exec(c))return c}var f=[];Object.entries(Ct).forEach(function(g){var h=p(g);g=h.next().value;h=h.next().value;b!==g&&f.push(h)});
d=new RegExp(f.join("|"));a.sort(function(g,h){return g.length-h.length});
e=p(a);for(c=e.next();!c.done;c=e.next())if(c=c.value,!d.exec(c))return c;return a[0]}
;function Et(){}
Et.prototype.m=function(a,b,c){b=void 0===b?{}:b;c=void 0===c?pt:c;var d=a.clickTrackingParams,e=this.l,f=!1;f=void 0===f?!1:f;e=void 0===e?!1:e;var g=L("INNERTUBE_CONTEXT");if(g){g=xb(g);M("web_no_tracking_params_in_shell_killswitch")||delete g.clickTracking;g.client||(g.client={});var h=g.client;"MWEB"===h.clientName&&(h.clientFormFactor=L("IS_TABLET")?"LARGE_FORM_FACTOR":"SMALL_FORM_FACTOR");h.screenWidthPoints=window.innerWidth;h.screenHeightPoints=window.innerHeight;h.screenPixelDensity=Math.round(window.devicePixelRatio||
1);h.screenDensityFloat=window.devicePixelRatio||1;h.utcOffsetMinutes=-Math.floor((new Date).getTimezoneOffset());var l=void 0===l?!1:l;am.getInstance();var m="USER_INTERFACE_THEME_LIGHT";dm(165)?m="USER_INTERFACE_THEME_DARK":dm(174)?m="USER_INTERFACE_THEME_LIGHT":!M("kevlar_legacy_browsers")&&window.matchMedia&&window.matchMedia("(prefers-color-scheme)").matches&&window.matchMedia("(prefers-color-scheme: dark)").matches&&(m="USER_INTERFACE_THEME_DARK");l=l?m:rt()||m;h.userInterfaceTheme=l;if(!f){if(l=
km())h.connectionType=l;M("web_log_effective_connection_type")&&(l=lm())&&(g.client.effectiveConnectionType=l)}var q;if(M("web_log_memory_total_kbytes")&&(null==(q=y.navigator)?0:q.deviceMemory)){var r;q=null==(r=y.navigator)?void 0:r.deviceMemory;g.client.memoryTotalKbytes=""+1E6*q}r=ll(y.location.href);!M("web_populate_internal_geo_killswitch")&&r.internalcountrycode&&(h.internalGeo=r.internalcountrycode);"MWEB"===h.clientName||"WEB"===h.clientName?(h.mainAppWebInfo={graftUrl:y.location.href},M("kevlar_woffle")&&
Vl.h&&(r=Vl.h,h.mainAppWebInfo.pwaInstallabilityStatus=!r.h&&r.i?"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED":"PWA_INSTALLABILITY_STATUS_UNKNOWN"),h.mainAppWebInfo.webDisplayMode=Wl(),h.mainAppWebInfo.isWebNativeShareAvailable=navigator&&void 0!==navigator.share):"TVHTML5"===h.clientName&&(!M("web_lr_app_quality_killswitch")&&(r=L("LIVING_ROOM_APP_QUALITY"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||{},{appQuality:r})),r=L("LIVING_ROOM_CERTIFICATION_SCOPE"))&&(h.tvAppInfo=Object.assign(h.tvAppInfo||
{},{certificationScope:r}));if(!M("web_populate_time_zone_itc_killswitch")){b:{if("undefined"!==typeof Intl)try{var w=(new Intl.DateTimeFormat).resolvedOptions().timeZone;break b}catch(rb){}w=void 0}w&&(h.timeZone=w)}(w=Vk())?h.experimentsToken=w:delete h.experimentsToken;w=Wk();st.h||(st.h=new st);h=st.h.h;r=[];q=0;for(var t in h)r[q++]=h[t];g.request=Object.assign({},g.request,{internalExperimentFlags:w,consistencyTokenJars:r});!M("web_prequest_context_killswitch")&&(t=L("INNERTUBE_CONTEXT_PREQUEST_CONTEXT"))&&
(g.request.externalPrequestContext=t);w=am.getInstance();t=dm(58);w=w.get("gsml","");g.user=Object.assign({},g.user);t&&(g.user.enableSafetyMode=t);w&&(g.user.lockedSafetyMode=!0);M("warm_op_csn_cleanup")?e&&(f=Ms())&&(g.clientScreenNonce=f):!f&&(f=Ms())&&(g.clientScreenNonce=f);d&&(g.clickTracking={clickTrackingParams:d});if(d=B("yt.mdx.remote.remoteClient_"))g.remoteClient=d;vt.getInstance().setLocationOnInnerTubeContext(g);try{var A=ol(),E=A.bid;delete A.bid;g.adSignalsInfo={params:[],bid:E};var F=
p(Object.entries(A));for(var O=F.next();!O.done;O=F.next()){var N=p(O.value),R=N.next().value,ca=N.next().value;A=R;E=ca;d=void 0;null==(d=g.adSignalsInfo.params)||d.push({key:A,value:""+E})}}catch(rb){ts(rb)}F=g}else ts(Error("Error: No InnerTubeContext shell provided in ytconfig.")),F={};F={context:F};if(O=this.h(a)){this.i(F,O,b);var U;b="/youtubei/v1/"+Dt(this.j());(O=null==(U=nr(a.commandMetadata,oj))?void 0:U.apiUrl)&&(b=O);U=b;(b=L("INNERTUBE_HOST_OVERRIDE"))&&(U=String(b)+String(qc(U)));b=
{};b.key=L("INNERTUBE_API_KEY");M("json_condensed_response")&&(b.prettyPrint="false");U=ml(U,b||{},!1);a=Object.assign({},{command:a},void 0);a={input:U,xa:$s(U),ha:F,config:a};a.config.ab?a.config.ab.identity=c:a.config.ab={identity:c};return a}ts(new P("Error: Failed to create Request from Command.",a))};
fa.Object.defineProperties(Et.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!1}}});function Ft(){}
u(Ft,Et);Ft.prototype.m=function(){return{input:"/getDatasyncIdsEndpoint",xa:$s("/getDatasyncIdsEndpoint","GET"),ha:{}}};
Ft.prototype.j=function(){return[]};
Ft.prototype.h=function(){};
Ft.prototype.i=function(){};var Gt={},Ht=(Gt.GET_DATASYNC_IDS=At(Ft),Gt);function It(a){var b=Ka.apply(1,arguments);if(!Jt(a)||b.some(function(d){return!Jt(d)}))throw Error("Only objects may be merged.");
b=p(b);for(var c=b.next();!c.done;c=b.next())Kt(a,c.value);return a}
function Kt(a,b){for(var c in b)if(Jt(b[c])){if(c in a&&!Jt(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Kt(a[c],b[c])}else if(Lt(b[c])){if(c in a&&!Lt(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Mt(a[c],b[c])}else a[c]=b[c];return a}
function Mt(a,b){b=p(b);for(var c=b.next();!c.done;c=b.next())c=c.value,Jt(c)?a.push(Kt({},c)):Lt(c)?a.push(Mt([],c)):a.push(c);return a}
function Jt(a){return"object"===typeof a&&!Array.isArray(a)}
function Lt(a){return"object"===typeof a&&Array.isArray(a)}
;function Nt(a,b){Ro.call(this,1,arguments);this.timer=b}
u(Nt,Ro);var Ot=new So("aft-recorded",Nt);var Pt=window;function Qt(){this.timing={};this.clearResourceTimings=function(){};
this.webkitClearResourceTimings=function(){};
this.mozClearResourceTimings=function(){};
this.msClearResourceTimings=function(){};
this.oClearResourceTimings=function(){}}
var S=Pt.performance||Pt.mozPerformance||Pt.msPerformance||Pt.webkitPerformance||new Qt;var Rt=!1,St={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",
'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",'script[name="mobile_blazer_watch_mod"]':"mbwj"};
Za(S.clearResourceTimings||S.webkitClearResourceTimings||S.mozClearResourceTimings||S.msClearResourceTimings||S.oClearResourceTimings||eb,S);function Tt(a){var b=Ut("aft",a);if(b)return b;b=L((a||"")+"TIMING_AFT_KEYS",["ol"]);for(var c=b.length,d=0;d<c;d++){var e=Ut(b[d],a);if(e)return e}return NaN}
function Vt(){var a;if(M("csi_use_performance_navigation_timing")||M("csi_use_performance_navigation_timing_tvhtml5")){var b,c,d,e=null==S?void 0:null==(a=S.getEntriesByType)?void 0:null==(b=a.call(S,"navigation"))?void 0:null==(c=b[0])?void 0:null==(d=c.toJSON)?void 0:d.call(c);e?(e.requestStart=Wt(e.requestStart),e.responseEnd=Wt(e.responseEnd),e.redirectStart=Wt(e.redirectStart),e.redirectEnd=Wt(e.redirectEnd),e.domainLookupEnd=Wt(e.domainLookupEnd),e.connectStart=Wt(e.connectStart),e.connectEnd=
Wt(e.connectEnd),e.responseStart=Wt(e.responseStart),e.secureConnectionStart=Wt(e.secureConnectionStart),e.domainLookupStart=Wt(e.domainLookupStart),e.isPerformanceNavigationTiming=!0,a=e):a=S.timing}else a=S.timing;return a}
function Xt(){return(M("csi_use_time_origin")||M("csi_use_time_origin_tvhtml5"))&&S.timeOrigin?Math.floor(S.timeOrigin):S.timing.navigationStart}
function Wt(a){return Math.round(Xt()+a)}
function Yt(a){var b;(b=B("ytcsi."+(a||"")+"data_"))||(b={tick:{},info:{}},z("ytcsi."+(a||"")+"data_",b));return b}
function Zt(a){a=Yt(a);a.info||(a.info={});return a.info}
function $t(a){a=Yt(a);a.metadata||(a.metadata={});return a.metadata}
function au(a){a=Yt(a);a.tick||(a.tick={});return a.tick}
function Ut(a,b){if(a=au(b)[a])return"number"===typeof a?a:a[a.length-1]}
function bu(a){a=Yt(a);if(a.gel){var b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function cu(a){a=bu(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
function du(a){var b=Yt(a).nonce;b||(b=Bs(),Yt(a).nonce=b);return b}
function eu(a){var b=Ut("_start",a),c=Tt(a);b&&c&&!Rt&&(Xo(Ot,new Nt(Math.round(c-b),a)),Rt=!0)}
function fu(a,b){for(var c=p(Object.keys(b)),d=c.next();!d.done;d=c.next())if(d=d.value,!Object.keys(a).includes(d)||"object"===typeof b[d]&&!fu(a[d],b[d]))return!1;return!0}
;function gu(){if(S.getEntriesByType){var a=S.getEntriesByType("paint");if(a=lb(a,function(b){return"first-paint"===b.name}))return Wt(a.startTime)}a=S.timing;
return a.Zc?Math.max(0,a.Zc):0}
;function hu(){var a=B("ytcsi.debug");a||(a=[],z("ytcsi.debug",a),z("ytcsi.reference",{}));return a}
function iu(a){a=a||"";var b=B("ytcsi.reference");b||(hu(),b=B("ytcsi.reference"));if(b[a])return b[a];var c=hu(),d={timerName:a,info:{},tick:{},span:{},jspbInfo:[]};c.push(d);return b[a]=d}
;var T={},ju=(T.auto_search="LATENCY_ACTION_AUTO_SEARCH",T.ad_to_ad="LATENCY_ACTION_AD_TO_AD",T.ad_to_video="LATENCY_ACTION_AD_TO_VIDEO",T["analytics.explore"]="LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE",T.app_startup="LATENCY_ACTION_APP_STARTUP",T["artist.analytics"]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS",T["artist.events"]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS",T["artist.presskit"]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE",T["song.analytics"]="LATENCY_ACTION_CREATOR_SONG_ANALYTICS",T.browse="LATENCY_ACTION_BROWSE",
T.cast_splash="LATENCY_ACTION_CAST_SPLASH",T.channels="LATENCY_ACTION_CHANNELS",T.creator_channel_dashboard="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD",T["channel.analytics"]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS",T["channel.comments"]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS",T["channel.content"]="LATENCY_ACTION_CREATOR_POST_LIST",T["channel.content.promotions"]="LATENCY_ACTION_CREATOR_PROMOTION_LIST",T["channel.copyright"]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT",T["channel.editing"]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING",
T["channel.monetization"]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION",T["channel.music"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC",T["channel.music_storefront"]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT",T["channel.playlists"]="LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS",T["channel.translations"]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS",T["channel.videos"]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS",T["channel.live_streaming"]="LATENCY_ACTION_CREATOR_LIVE_STREAMING",T.chips="LATENCY_ACTION_CHIPS",
T["dialog.copyright_strikes"]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES",T["dialog.video_copyright"]="LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT",T["dialog.uploads"]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS",T.direct_playback="LATENCY_ACTION_DIRECT_PLAYBACK",T.embed="LATENCY_ACTION_EMBED",T.entity_key_serialization_perf="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",T.entity_key_deserialization_perf="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",T.explore="LATENCY_ACTION_EXPLORE",T.home=
"LATENCY_ACTION_HOME",T.library="LATENCY_ACTION_LIBRARY",T.live="LATENCY_ACTION_LIVE",T.live_pagination="LATENCY_ACTION_LIVE_PAGINATION",T.onboarding="LATENCY_ACTION_ONBOARDING",T.owner="LATENCY_ACTION_CREATOR_CMS_DASHBOARD",T["owner.analytics"]="LATENCY_ACTION_CREATOR_CMS_ANALYTICS",T["owner.assets"]="LATENCY_ACTION_CREATOR_CMS_ASSETS",T["owner.channels"]="LATENCY_ACTION_CREATOR_CMS_CHANNELS",T["owner.claimed_videos"]="LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS",T["owner.claims"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",
T["owner.claims.manual"]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING",T["owner.delivery"]="LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY",T["owner.issues"]="LATENCY_ACTION_CREATOR_CMS_ISSUES",T["owner.reports"]="LATENCY_ACTION_CREATOR_CMS_REPORTS",T["owner.videos"]="LATENCY_ACTION_CREATOR_CMS_VIDEOS",T.parent_profile_settings="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",T.parent_tools_collection="LATENCY_ACTION_PARENT_TOOLS_COLLECTION",T.parent_tools_dashboard="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",
T.player_att="LATENCY_ACTION_PLAYER_ATTESTATION",T["post.comments"]="LATENCY_ACTION_CREATOR_POST_COMMENTS",T["post.edit"]="LATENCY_ACTION_CREATOR_POST_EDIT",T.prebuffer="LATENCY_ACTION_PREBUFFER",T.prefetch="LATENCY_ACTION_PREFETCH",T.profile_settings="LATENCY_ACTION_KIDS_PROFILE_SETTINGS",T.profile_switcher="LATENCY_ACTION_LOGIN",T.reel_watch="LATENCY_ACTION_REEL_WATCH",T.results="LATENCY_ACTION_RESULTS",T["promotion.edit"]="LATENCY_ACTION_CREATOR_PROMOTION_EDIT",T.search_ui="LATENCY_ACTION_SEARCH_UI",
T.search_suggest="LATENCY_ACTION_SUGGEST",T.search_zero_state="LATENCY_ACTION_SEARCH_ZERO_STATE",T.secret_code="LATENCY_ACTION_KIDS_SECRET_CODE",T.seek="LATENCY_ACTION_PLAYER_SEEK",T.settings="LATENCY_ACTION_SETTINGS",T.store="LATENCY_ACTION_STORE",T.tenx="LATENCY_ACTION_TENX",T.video_to_ad="LATENCY_ACTION_VIDEO_TO_AD",T.watch="LATENCY_ACTION_WATCH",T.watch_it_again="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN",T["watch,watch7"]="LATENCY_ACTION_WATCH",T["watch,watch7_html5"]="LATENCY_ACTION_WATCH",T["watch,watch7ad"]=
"LATENCY_ACTION_WATCH",T["watch,watch7ad_html5"]="LATENCY_ACTION_WATCH",T.wn_comments="LATENCY_ACTION_LOAD_COMMENTS",T.ww_rqs="LATENCY_ACTION_WHO_IS_WATCHING",T["video.analytics"]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS",T["video.comments"]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS",T["video.edit"]="LATENCY_ACTION_CREATOR_VIDEO_EDIT",T["video.editor"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR",T["video.editor_async"]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC",T["video.live_settings"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS",
T["video.live_streaming"]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING",T["video.monetization"]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION",T["video.translations"]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS",T.voice_assistant="LATENCY_ACTION_VOICE_ASSISTANT",T.cast_load_by_entity_to_watch="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",T.networkless_performance="LATENCY_ACTION_NETWORKLESS_PERFORMANCE",T),V={},ku=(V.ad_allowed="adTypesAllowed",V.yt_abt="adBreakType",V.ad_cpn="adClientPlaybackNonce",
V.ad_docid="adVideoId",V.yt_ad_an="adNetworks",V.ad_at="adType",V.aida="appInstallDataAgeMs",V.browse_id="browseId",V.p="httpProtocol",V.t="transportProtocol",V.cs="commandSource",V.cpn="clientPlaybackNonce",V.ccs="creatorInfo.creatorCanaryState",V.ctop="creatorInfo.topEntityType",V.csn="clientScreenNonce",V.docid="videoId",V.GetHome_rid="requestIds",V.GetSearch_rid="requestIds",V.GetPlayer_rid="requestIds",V.GetWatchNext_rid="requestIds",V.GetBrowse_rid="requestIds",V.GetLibrary_rid="requestIds",
V.is_continuation="isContinuation",V.is_nav="isNavigation",V.b_p="kabukiInfo.browseParams",V.is_prefetch="kabukiInfo.isPrefetch",V.is_secondary_nav="kabukiInfo.isSecondaryNav",V.nav_type="kabukiInfo.navigationType",V.prev_browse_id="kabukiInfo.prevBrowseId",V.query_source="kabukiInfo.querySource",V.voz_type="kabukiInfo.vozType",V.yt_lt="loadType",V.mver="creatorInfo.measurementVersion",V.yt_ad="isMonetized",V.nr="webInfo.navigationReason",V.nrsu="navigationRequestedSameUrl",V.pnt="performanceNavigationTiming",
V.prt="playbackRequiresTap",V.plt="playerInfo.playbackType",V.pis="playerInfo.playerInitializedState",V.paused="playerInfo.isPausedOnLoad",V.yt_pt="playerType",V.fmt="playerInfo.itag",V.yt_pl="watchInfo.isPlaylist",V.yt_pre="playerInfo.preloadType",V.yt_ad_pr="prerollAllowed",V.pa="previousAction",V.yt_red="isRedSubscriber",V.rce="mwebInfo.responseContentEncoding",V.rc="resourceInfo.resourceCache",V.scrh="screenHeight",V.scrw="screenWidth",V.st="serverTimeMs",V.ssdm="shellStartupDurationMs",V.br_trs=
"tvInfo.bedrockTriggerState",V.kebqat="kabukiInfo.earlyBrowseRequestInfo.abandonmentType",V.kebqa="kabukiInfo.earlyBrowseRequestInfo.adopted",V.label="tvInfo.label",V.is_mdx="tvInfo.isMdx",V.preloaded="tvInfo.isPreloaded",V.aac_type="tvInfo.authAccessCredentialType",V.upg_player_vis="playerInfo.visibilityState",V.query="unpluggedInfo.query",V.upg_chip_ids_string="unpluggedInfo.upgChipIdsString",V.yt_vst="videoStreamType",V.vph="viewportHeight",V.vpw="viewportWidth",V.yt_vis="isVisible",V.rcl="mwebInfo.responseContentLength",
V.GetSettings_rid="requestIds",V.GetTrending_rid="requestIds",V.GetMusicSearchSuggestions_rid="requestIds",V.REQUEST_ID="requestIds",V),lu="isContinuation isNavigation kabukiInfo.earlyBrowseRequestInfo.adopted kabukiInfo.isPrefetch kabukiInfo.isSecondaryNav isMonetized navigationRequestedSameUrl performanceNavigationTiming playerInfo.isPausedOnLoad prerollAllowed isRedSubscriber tvInfo.isMdx tvInfo.isPreloaded isVisible watchInfo.isPlaylist playbackRequiresTap".split(" "),mu={},nu=(mu.ccs="CANARY_STATE_",
mu.mver="MEASUREMENT_VERSION_",mu.pis="PLAYER_INITIALIZED_STATE_",mu.yt_pt="LATENCY_PLAYER_",mu.pa="LATENCY_ACTION_",mu.ctop="TOP_ENTITY_TYPE_",mu.yt_vst="VIDEO_STREAM_TYPE_",mu),ou="all_vc ap aq c cbr cbrand cbrver cmodel cos cosver cplatform ctheme cver ei l_an l_mm plid srt yt_fss yt_li vpst vpni2 vpil2 icrc icrt pa GetAccountOverview_rid GetHistory_rid cmt d_vpct d_vpnfi d_vpni nsru pc pfa pfeh pftr pnc prerender psc rc start tcrt tcrc ssr vpr vps yt_abt yt_fn yt_fs yt_pft yt_pre yt_pt yt_pvis ytu_pvis yt_ref yt_sts tds".split(" ");
function pu(a){return ju[a]||"LATENCY_ACTION_UNKNOWN"}
function qu(a,b,c){c=bu(c);if(c.gelInfos)c.gelInfos[a]=!0;else{var d={};c.gelInfos=(d[a]=!0,d)}if(a.match("_rid")){var e=a.split("_rid")[0];a="REQUEST_ID"}if(a in ku){c=ku[a];0<=gb(lu,c)&&(b=!!b);a in nu&&"string"===typeof b&&(b=nu[a]+b.toUpperCase());a=b;b=c.split(".");for(var f=d={},g=0;g<b.length-1;g++){var h=b[g];f[h]={};f=f[h]}f[b[b.length-1]]="requestIds"===c?[{id:a,endpoint:e}]:a;return It({},d)}0<=gb(ou,a)||us(new P("Unknown label logged with GEL CSI",a))}
;var W={LATENCY_ACTION_SHORTS_VIDEO_INGESTION_TRANSCODING:179,LATENCY_ACTION_KIDS_PROFILE_SWITCHER:90,LATENCY_ACTION_OFFLINE_THUMBNAIL_TRANSFER:100,LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC:46,LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR:37,LATENCY_ACTION_SPINNER_DISPLAYED:14,LATENCY_ACTION_PLAYABILITY_CHECK:10,LATENCY_ACTION_PROCESS:9,LATENCY_ACTION_APP_STARTUP:5,LATENCY_ACTION_COMMERCE_ACTION_COMMAND_RPC:203,LATENCY_ACTION_COMMERCE_TRANSACTION:184,LATENCY_ACTION_LOG_PAYMENT_SERVER_ANALYTICS_RPC:173,
LATENCY_ACTION_GET_PAYMENT_INSTRUMENTS_PARAMS_RPC:172,LATENCY_ACTION_GET_FIX_INSTRUMENT_PARAMS_RPC:171,LATENCY_ACTION_RESUME_SUBSCRIPTION_RPC:170,LATENCY_ACTION_PAUSE_SUBSCRIPTION_RPC:169,LATENCY_ACTION_GET_OFFLINE_UPSELL_RPC:168,LATENCY_ACTION_GET_OFFERS_RPC:167,LATENCY_ACTION_GET_CANCELLATION_YT_FLOW_RPC:166,LATENCY_ACTION_GET_CANCELLATION_FLOW_RPC:165,LATENCY_ACTION_UPDATE_CROSS_DEVICE_OFFLINE_STATE_RPC:164,LATENCY_ACTION_GET_OFFER_DETAILS_RPC:163,LATENCY_ACTION_CANCEL_RECURRENCE_TRANSACTION_RPC:162,
LATENCY_ACTION_GET_TIP_MODULE_RPC:161,LATENCY_ACTION_HANDLE_TRANSACTION_RPC:160,LATENCY_ACTION_COMPLETE_TRANSACTION_RPC:159,LATENCY_ACTION_GET_CART_RPC:158,LATENCY_ACTION_THUMBNAIL_FETCH:156,LATENCY_ACTION_ABANDONED_DIRECT_PLAYBACK:154,LATENCY_ACTION_SHARE_VIDEO:153,LATENCY_ACTION_AD_TO_VIDEO_INT:152,LATENCY_ACTION_ABANDONED_BROWSE:151,LATENCY_ACTION_PLAYER_ROTATION:150,LATENCY_ACTION_GENERIC_WEB_VIEW:183,LATENCY_ACTION_SHOPPING_IN_APP:124,LATENCY_ACTION_PLAYER_ATTESTATION:121,LATENCY_ACTION_PLAYER_SEEK:119,
LATENCY_ACTION_SUPER_STICKER_BUY_FLOW:114,LATENCY_ACTION_DOWNLOADS_DATA_ACCESS:180,LATENCY_ACTION_BLOCKS_PERFORMANCE:148,LATENCY_ACTION_ASSISTANT_QUERY:138,LATENCY_ACTION_ASSISTANT_SETTINGS:137,LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF:129,LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF:128,LATENCY_ACTION_PROOF_OF_ORIGIN_TOKEN_CREATE:127,LATENCY_ACTION_EMBEDS_SDK_INITIALIZATION:123,LATENCY_ACTION_NETWORKLESS_PERFORMANCE:122,LATENCY_ACTION_DOWNLOADS_EXPANSION:133,LATENCY_ACTION_ENTITY_TRANSFORM:131,
LATENCY_ACTION_DOWNLOADS_COMPATIBILITY_LAYER:96,LATENCY_ACTION_EMBEDS_SET_VIDEO:95,LATENCY_ACTION_SETTINGS:93,LATENCY_ACTION_ABANDONED_STARTUP:81,LATENCY_ACTION_MEDIA_BROWSER_ALARM_PLAY:80,LATENCY_ACTION_MEDIA_BROWSER_SEARCH:79,LATENCY_ACTION_MEDIA_BROWSER_LOAD_TREE:78,LATENCY_ACTION_WHO_IS_WATCHING:77,LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH:76,LATENCY_ACTION_LITE_SWITCH_ACCOUNT:73,LATENCY_ACTION_ELEMENTS_PERFORMANCE:70,LATENCY_ACTION_LOCATION_SIGNAL_COLLECTION:69,LATENCY_ACTION_MODIFY_CHANNEL_NOTIFICATION:65,
LATENCY_ACTION_OFFLINE_STORE_START:61,LATENCY_ACTION_REEL_EDITOR:58,LATENCY_ACTION_CHANNEL_SUBSCRIBE:56,LATENCY_ACTION_CHANNEL_PREVIEW:55,LATENCY_ACTION_PREFETCH:52,LATENCY_ACTION_ABANDONED_WATCH:45,LATENCY_ACTION_LOAD_COMMENT_REPLIES:26,LATENCY_ACTION_LOAD_COMMENTS:25,LATENCY_ACTION_EDIT_COMMENT:24,LATENCY_ACTION_NEW_COMMENT:23,LATENCY_ACTION_OFFLINE_SHARING_RECEIVER_PAIRING:19,LATENCY_ACTION_EMBED:18,LATENCY_ACTION_MDX_LAUNCH:15,LATENCY_ACTION_RESOLVE_URL:13,LATENCY_ACTION_CAST_SPLASH:149,LATENCY_ACTION_MDX_CONNECT_TO_SESSION:190,
LATENCY_ACTION_MDX_STREAM_TRANSFER:178,LATENCY_ACTION_MDX_CAST:120,LATENCY_ACTION_MDX_COMMAND:12,LATENCY_ACTION_REEL_SELECT_SEGMENT:136,LATENCY_ACTION_ACCELERATED_EFFECTS:145,LATENCY_ACTION_EDIT_AUDIO_GEN:182,LATENCY_ACTION_UPLOAD_AUDIO_MIXER:147,LATENCY_ACTION_SHORTS_CLIENT_SIDE_RENDERING:157,LATENCY_ACTION_SHORTS_SEG_IMP_TRANSCODING:146,LATENCY_ACTION_SHORTS_AUDIO_PICKER_PLAYBACK:130,LATENCY_ACTION_SHORTS_WAVEFORM_DOWNLOAD:125,LATENCY_ACTION_SHORTS_VIDEO_INGESTION:155,LATENCY_ACTION_SHORTS_GALLERY:107,
LATENCY_ACTION_SHORTS_TRIM:105,LATENCY_ACTION_SHORTS_EDIT:104,LATENCY_ACTION_SHORTS_CAMERA:103,LATENCY_ACTION_PRODUCER_EXPORT_PROJECT:193,LATENCY_ACTION_PRODUCER_EDITOR:192,LATENCY_ACTION_PARENT_TOOLS_DASHBOARD:102,LATENCY_ACTION_PARENT_TOOLS_COLLECTION:101,LATENCY_ACTION_MUSIC_LOAD_RECOMMENDED_MEDIA_ITEMS:116,LATENCY_ACTION_MUSIC_LOAD_MEDIA_ITEMS:115,LATENCY_ACTION_MUSIC_ALBUM_DETAIL:72,LATENCY_ACTION_MUSIC_PLAYLIST_DETAIL:71,LATENCY_ACTION_STORE:175,LATENCY_ACTION_CHIPS:68,LATENCY_ACTION_SEARCH_ZERO_STATE:67,
LATENCY_ACTION_LIVE_PAGINATION:117,LATENCY_ACTION_LIVE:20,LATENCY_ACTION_PREBUFFER:40,LATENCY_ACTION_TENX:39,LATENCY_ACTION_KIDS_PROFILE_SETTINGS:94,LATENCY_ACTION_KIDS_WATCH_IT_AGAIN:92,LATENCY_ACTION_KIDS_SECRET_CODE:91,LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS:89,LATENCY_ACTION_KIDS_ONBOARDING:88,LATENCY_ACTION_KIDS_VOICE_SEARCH:82,LATENCY_ACTION_KIDS_CURATED_COLLECTION:62,LATENCY_ACTION_KIDS_LIBRARY:53,LATENCY_ACTION_CREATOR_PROMOTION_LIST:186,LATENCY_ACTION_CREATOR_PROMOTION_EDIT:185,LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS:38,
LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION:74,LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING:141,LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS:142,LATENCY_ACTION_CREATOR_VIDEO_EDITOR_ASYNC:51,LATENCY_ACTION_CREATOR_VIDEO_EDITOR:50,LATENCY_ACTION_CREATOR_VIDEO_EDIT:36,LATENCY_ACTION_CREATOR_VIDEO_COMMENTS:34,LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS:33,LATENCY_ACTION_CREATOR_SONG_ANALYTICS:176,LATENCY_ACTION_CREATOR_POST_LIST:112,LATENCY_ACTION_CREATOR_POST_EDIT:110,LATENCY_ACTION_CREATOR_POST_COMMENTS:111,
LATENCY_ACTION_CREATOR_LIVE_STREAMING:108,LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT:174,LATENCY_ACTION_CREATOR_DIALOG_UPLOADS:86,LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES:87,LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS:32,LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS:48,LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS:139,LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT:177,LATENCY_ACTION_CREATOR_CHANNEL_MUSIC:99,LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION:43,LATENCY_ACTION_CREATOR_CHANNEL_EDITING:113,LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD:49,
LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT:44,LATENCY_ACTION_CREATOR_CMS_VIDEOS:202,LATENCY_ACTION_CREATOR_CMS_REPORTS:201,LATENCY_ACTION_CREATOR_CMS_ISSUES:191,LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING:200,LATENCY_ACTION_CREATOR_CMS_DASHBOARD:199,LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY:198,LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS:197,LATENCY_ACTION_CREATOR_CMS_CHANNELS:196,LATENCY_ACTION_CREATOR_CMS_ASSETS:195,LATENCY_ACTION_CREATOR_CMS_ANALYTICS:194,LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS:66,
LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS:31,LATENCY_ACTION_CREATOR_ARTIST_PROFILE:85,LATENCY_ACTION_CREATOR_ARTIST_CONCERTS:84,LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS:83,LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE:140,LATENCY_ACTION_EXPERIMENTAL_WATCH_UI:181,LATENCY_ACTION_STORYBOARD_THUMBNAILS:118,LATENCY_ACTION_SEARCH_THUMBNAILS:59,LATENCY_ACTION_ON_DEVICE_MODEL_DOWNLOAD:54,LATENCY_ACTION_VOICE_ASSISTANT:47,LATENCY_ACTION_SEARCH_UI:35,LATENCY_ACTION_SUGGEST:30,LATENCY_ACTION_AUTO_SEARCH:126,LATENCY_ACTION_DOWNLOADS:98,
LATENCY_ACTION_EXPLORE:75,LATENCY_ACTION_VIDEO_LIST:63,LATENCY_ACTION_HOME_RESUME:60,LATENCY_ACTION_SUBSCRIPTIONS_LIST:57,LATENCY_ACTION_THUMBNAIL_LOAD:42,LATENCY_ACTION_FIRST_THUMBNAIL_LOAD:29,LATENCY_ACTION_SUBSCRIPTIONS_FEED:109,LATENCY_ACTION_SUBSCRIPTIONS:28,LATENCY_ACTION_TRENDING:27,LATENCY_ACTION_LIBRARY:21,LATENCY_ACTION_VIDEO_THUMBNAIL:8,LATENCY_ACTION_SHOW_MORE:7,LATENCY_ACTION_VIDEO_PREVIEW:6,LATENCY_ACTION_AD_TO_AD:22,LATENCY_ACTION_VIDEO_TO_AD:17,LATENCY_ACTION_AD_TO_VIDEO:16,LATENCY_ACTION_DIRECT_PLAYBACK:132,
LATENCY_ACTION_PREBUFFER_VIDEO:144,LATENCY_ACTION_PREFETCH_VIDEO:143,LATENCY_ACTION_STARTUP:106,LATENCY_ACTION_ONBOARDING:135,LATENCY_ACTION_LOGIN:97,LATENCY_ACTION_REEL_WATCH:41,LATENCY_ACTION_WATCH:3,LATENCY_ACTION_RESULTS:2,LATENCY_ACTION_CHANNELS:4,LATENCY_ACTION_HOME:1,LATENCY_ACTION_BROWSE:11,LATENCY_ACTION_USER_ACTION:189,LATENCY_ACTION_INFRASTRUCTURE:188,LATENCY_ACTION_PAGE_NAVIGATION:187,LATENCY_ACTION_UNKNOWN:0};W[W.LATENCY_ACTION_SHORTS_VIDEO_INGESTION_TRANSCODING]="LATENCY_ACTION_SHORTS_VIDEO_INGESTION_TRANSCODING";
W[W.LATENCY_ACTION_KIDS_PROFILE_SWITCHER]="LATENCY_ACTION_KIDS_PROFILE_SWITCHER";W[W.LATENCY_ACTION_OFFLINE_THUMBNAIL_TRANSFER]="LATENCY_ACTION_OFFLINE_THUMBNAIL_TRANSFER";W[W.LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR_ASYNC";W[W.LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR]="LATENCY_ACTION_CREATOR_VIDEO_VIDEO_EDITOR";W[W.LATENCY_ACTION_SPINNER_DISPLAYED]="LATENCY_ACTION_SPINNER_DISPLAYED";W[W.LATENCY_ACTION_PLAYABILITY_CHECK]="LATENCY_ACTION_PLAYABILITY_CHECK";
W[W.LATENCY_ACTION_PROCESS]="LATENCY_ACTION_PROCESS";W[W.LATENCY_ACTION_APP_STARTUP]="LATENCY_ACTION_APP_STARTUP";W[W.LATENCY_ACTION_COMMERCE_ACTION_COMMAND_RPC]="LATENCY_ACTION_COMMERCE_ACTION_COMMAND_RPC";W[W.LATENCY_ACTION_COMMERCE_TRANSACTION]="LATENCY_ACTION_COMMERCE_TRANSACTION";W[W.LATENCY_ACTION_LOG_PAYMENT_SERVER_ANALYTICS_RPC]="LATENCY_ACTION_LOG_PAYMENT_SERVER_ANALYTICS_RPC";W[W.LATENCY_ACTION_GET_PAYMENT_INSTRUMENTS_PARAMS_RPC]="LATENCY_ACTION_GET_PAYMENT_INSTRUMENTS_PARAMS_RPC";
W[W.LATENCY_ACTION_GET_FIX_INSTRUMENT_PARAMS_RPC]="LATENCY_ACTION_GET_FIX_INSTRUMENT_PARAMS_RPC";W[W.LATENCY_ACTION_RESUME_SUBSCRIPTION_RPC]="LATENCY_ACTION_RESUME_SUBSCRIPTION_RPC";W[W.LATENCY_ACTION_PAUSE_SUBSCRIPTION_RPC]="LATENCY_ACTION_PAUSE_SUBSCRIPTION_RPC";W[W.LATENCY_ACTION_GET_OFFLINE_UPSELL_RPC]="LATENCY_ACTION_GET_OFFLINE_UPSELL_RPC";W[W.LATENCY_ACTION_GET_OFFERS_RPC]="LATENCY_ACTION_GET_OFFERS_RPC";W[W.LATENCY_ACTION_GET_CANCELLATION_YT_FLOW_RPC]="LATENCY_ACTION_GET_CANCELLATION_YT_FLOW_RPC";
W[W.LATENCY_ACTION_GET_CANCELLATION_FLOW_RPC]="LATENCY_ACTION_GET_CANCELLATION_FLOW_RPC";W[W.LATENCY_ACTION_UPDATE_CROSS_DEVICE_OFFLINE_STATE_RPC]="LATENCY_ACTION_UPDATE_CROSS_DEVICE_OFFLINE_STATE_RPC";W[W.LATENCY_ACTION_GET_OFFER_DETAILS_RPC]="LATENCY_ACTION_GET_OFFER_DETAILS_RPC";W[W.LATENCY_ACTION_CANCEL_RECURRENCE_TRANSACTION_RPC]="LATENCY_ACTION_CANCEL_RECURRENCE_TRANSACTION_RPC";W[W.LATENCY_ACTION_GET_TIP_MODULE_RPC]="LATENCY_ACTION_GET_TIP_MODULE_RPC";
W[W.LATENCY_ACTION_HANDLE_TRANSACTION_RPC]="LATENCY_ACTION_HANDLE_TRANSACTION_RPC";W[W.LATENCY_ACTION_COMPLETE_TRANSACTION_RPC]="LATENCY_ACTION_COMPLETE_TRANSACTION_RPC";W[W.LATENCY_ACTION_GET_CART_RPC]="LATENCY_ACTION_GET_CART_RPC";W[W.LATENCY_ACTION_THUMBNAIL_FETCH]="LATENCY_ACTION_THUMBNAIL_FETCH";W[W.LATENCY_ACTION_ABANDONED_DIRECT_PLAYBACK]="LATENCY_ACTION_ABANDONED_DIRECT_PLAYBACK";W[W.LATENCY_ACTION_SHARE_VIDEO]="LATENCY_ACTION_SHARE_VIDEO";W[W.LATENCY_ACTION_AD_TO_VIDEO_INT]="LATENCY_ACTION_AD_TO_VIDEO_INT";
W[W.LATENCY_ACTION_ABANDONED_BROWSE]="LATENCY_ACTION_ABANDONED_BROWSE";W[W.LATENCY_ACTION_PLAYER_ROTATION]="LATENCY_ACTION_PLAYER_ROTATION";W[W.LATENCY_ACTION_GENERIC_WEB_VIEW]="LATENCY_ACTION_GENERIC_WEB_VIEW";W[W.LATENCY_ACTION_SHOPPING_IN_APP]="LATENCY_ACTION_SHOPPING_IN_APP";W[W.LATENCY_ACTION_PLAYER_ATTESTATION]="LATENCY_ACTION_PLAYER_ATTESTATION";W[W.LATENCY_ACTION_PLAYER_SEEK]="LATENCY_ACTION_PLAYER_SEEK";W[W.LATENCY_ACTION_SUPER_STICKER_BUY_FLOW]="LATENCY_ACTION_SUPER_STICKER_BUY_FLOW";
W[W.LATENCY_ACTION_DOWNLOADS_DATA_ACCESS]="LATENCY_ACTION_DOWNLOADS_DATA_ACCESS";W[W.LATENCY_ACTION_BLOCKS_PERFORMANCE]="LATENCY_ACTION_BLOCKS_PERFORMANCE";W[W.LATENCY_ACTION_ASSISTANT_QUERY]="LATENCY_ACTION_ASSISTANT_QUERY";W[W.LATENCY_ACTION_ASSISTANT_SETTINGS]="LATENCY_ACTION_ASSISTANT_SETTINGS";W[W.LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF]="LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF";W[W.LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF]="LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF";
W[W.LATENCY_ACTION_PROOF_OF_ORIGIN_TOKEN_CREATE]="LATENCY_ACTION_PROOF_OF_ORIGIN_TOKEN_CREATE";W[W.LATENCY_ACTION_EMBEDS_SDK_INITIALIZATION]="LATENCY_ACTION_EMBEDS_SDK_INITIALIZATION";W[W.LATENCY_ACTION_NETWORKLESS_PERFORMANCE]="LATENCY_ACTION_NETWORKLESS_PERFORMANCE";W[W.LATENCY_ACTION_DOWNLOADS_EXPANSION]="LATENCY_ACTION_DOWNLOADS_EXPANSION";W[W.LATENCY_ACTION_ENTITY_TRANSFORM]="LATENCY_ACTION_ENTITY_TRANSFORM";W[W.LATENCY_ACTION_DOWNLOADS_COMPATIBILITY_LAYER]="LATENCY_ACTION_DOWNLOADS_COMPATIBILITY_LAYER";
W[W.LATENCY_ACTION_EMBEDS_SET_VIDEO]="LATENCY_ACTION_EMBEDS_SET_VIDEO";W[W.LATENCY_ACTION_SETTINGS]="LATENCY_ACTION_SETTINGS";W[W.LATENCY_ACTION_ABANDONED_STARTUP]="LATENCY_ACTION_ABANDONED_STARTUP";W[W.LATENCY_ACTION_MEDIA_BROWSER_ALARM_PLAY]="LATENCY_ACTION_MEDIA_BROWSER_ALARM_PLAY";W[W.LATENCY_ACTION_MEDIA_BROWSER_SEARCH]="LATENCY_ACTION_MEDIA_BROWSER_SEARCH";W[W.LATENCY_ACTION_MEDIA_BROWSER_LOAD_TREE]="LATENCY_ACTION_MEDIA_BROWSER_LOAD_TREE";W[W.LATENCY_ACTION_WHO_IS_WATCHING]="LATENCY_ACTION_WHO_IS_WATCHING";
W[W.LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH]="LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH";W[W.LATENCY_ACTION_LITE_SWITCH_ACCOUNT]="LATENCY_ACTION_LITE_SWITCH_ACCOUNT";W[W.LATENCY_ACTION_ELEMENTS_PERFORMANCE]="LATENCY_ACTION_ELEMENTS_PERFORMANCE";W[W.LATENCY_ACTION_LOCATION_SIGNAL_COLLECTION]="LATENCY_ACTION_LOCATION_SIGNAL_COLLECTION";W[W.LATENCY_ACTION_MODIFY_CHANNEL_NOTIFICATION]="LATENCY_ACTION_MODIFY_CHANNEL_NOTIFICATION";W[W.LATENCY_ACTION_OFFLINE_STORE_START]="LATENCY_ACTION_OFFLINE_STORE_START";
W[W.LATENCY_ACTION_REEL_EDITOR]="LATENCY_ACTION_REEL_EDITOR";W[W.LATENCY_ACTION_CHANNEL_SUBSCRIBE]="LATENCY_ACTION_CHANNEL_SUBSCRIBE";W[W.LATENCY_ACTION_CHANNEL_PREVIEW]="LATENCY_ACTION_CHANNEL_PREVIEW";W[W.LATENCY_ACTION_PREFETCH]="LATENCY_ACTION_PREFETCH";W[W.LATENCY_ACTION_ABANDONED_WATCH]="LATENCY_ACTION_ABANDONED_WATCH";W[W.LATENCY_ACTION_LOAD_COMMENT_REPLIES]="LATENCY_ACTION_LOAD_COMMENT_REPLIES";W[W.LATENCY_ACTION_LOAD_COMMENTS]="LATENCY_ACTION_LOAD_COMMENTS";
W[W.LATENCY_ACTION_EDIT_COMMENT]="LATENCY_ACTION_EDIT_COMMENT";W[W.LATENCY_ACTION_NEW_COMMENT]="LATENCY_ACTION_NEW_COMMENT";W[W.LATENCY_ACTION_OFFLINE_SHARING_RECEIVER_PAIRING]="LATENCY_ACTION_OFFLINE_SHARING_RECEIVER_PAIRING";W[W.LATENCY_ACTION_EMBED]="LATENCY_ACTION_EMBED";W[W.LATENCY_ACTION_MDX_LAUNCH]="LATENCY_ACTION_MDX_LAUNCH";W[W.LATENCY_ACTION_RESOLVE_URL]="LATENCY_ACTION_RESOLVE_URL";W[W.LATENCY_ACTION_CAST_SPLASH]="LATENCY_ACTION_CAST_SPLASH";W[W.LATENCY_ACTION_MDX_CONNECT_TO_SESSION]="LATENCY_ACTION_MDX_CONNECT_TO_SESSION";
W[W.LATENCY_ACTION_MDX_STREAM_TRANSFER]="LATENCY_ACTION_MDX_STREAM_TRANSFER";W[W.LATENCY_ACTION_MDX_CAST]="LATENCY_ACTION_MDX_CAST";W[W.LATENCY_ACTION_MDX_COMMAND]="LATENCY_ACTION_MDX_COMMAND";W[W.LATENCY_ACTION_REEL_SELECT_SEGMENT]="LATENCY_ACTION_REEL_SELECT_SEGMENT";W[W.LATENCY_ACTION_ACCELERATED_EFFECTS]="LATENCY_ACTION_ACCELERATED_EFFECTS";W[W.LATENCY_ACTION_EDIT_AUDIO_GEN]="LATENCY_ACTION_EDIT_AUDIO_GEN";W[W.LATENCY_ACTION_UPLOAD_AUDIO_MIXER]="LATENCY_ACTION_UPLOAD_AUDIO_MIXER";
W[W.LATENCY_ACTION_SHORTS_CLIENT_SIDE_RENDERING]="LATENCY_ACTION_SHORTS_CLIENT_SIDE_RENDERING";W[W.LATENCY_ACTION_SHORTS_SEG_IMP_TRANSCODING]="LATENCY_ACTION_SHORTS_SEG_IMP_TRANSCODING";W[W.LATENCY_ACTION_SHORTS_AUDIO_PICKER_PLAYBACK]="LATENCY_ACTION_SHORTS_AUDIO_PICKER_PLAYBACK";W[W.LATENCY_ACTION_SHORTS_WAVEFORM_DOWNLOAD]="LATENCY_ACTION_SHORTS_WAVEFORM_DOWNLOAD";W[W.LATENCY_ACTION_SHORTS_VIDEO_INGESTION]="LATENCY_ACTION_SHORTS_VIDEO_INGESTION";W[W.LATENCY_ACTION_SHORTS_GALLERY]="LATENCY_ACTION_SHORTS_GALLERY";
W[W.LATENCY_ACTION_SHORTS_TRIM]="LATENCY_ACTION_SHORTS_TRIM";W[W.LATENCY_ACTION_SHORTS_EDIT]="LATENCY_ACTION_SHORTS_EDIT";W[W.LATENCY_ACTION_SHORTS_CAMERA]="LATENCY_ACTION_SHORTS_CAMERA";W[W.LATENCY_ACTION_PRODUCER_EXPORT_PROJECT]="LATENCY_ACTION_PRODUCER_EXPORT_PROJECT";W[W.LATENCY_ACTION_PRODUCER_EDITOR]="LATENCY_ACTION_PRODUCER_EDITOR";W[W.LATENCY_ACTION_PARENT_TOOLS_DASHBOARD]="LATENCY_ACTION_PARENT_TOOLS_DASHBOARD";W[W.LATENCY_ACTION_PARENT_TOOLS_COLLECTION]="LATENCY_ACTION_PARENT_TOOLS_COLLECTION";
W[W.LATENCY_ACTION_MUSIC_LOAD_RECOMMENDED_MEDIA_ITEMS]="LATENCY_ACTION_MUSIC_LOAD_RECOMMENDED_MEDIA_ITEMS";W[W.LATENCY_ACTION_MUSIC_LOAD_MEDIA_ITEMS]="LATENCY_ACTION_MUSIC_LOAD_MEDIA_ITEMS";W[W.LATENCY_ACTION_MUSIC_ALBUM_DETAIL]="LATENCY_ACTION_MUSIC_ALBUM_DETAIL";W[W.LATENCY_ACTION_MUSIC_PLAYLIST_DETAIL]="LATENCY_ACTION_MUSIC_PLAYLIST_DETAIL";W[W.LATENCY_ACTION_STORE]="LATENCY_ACTION_STORE";W[W.LATENCY_ACTION_CHIPS]="LATENCY_ACTION_CHIPS";W[W.LATENCY_ACTION_SEARCH_ZERO_STATE]="LATENCY_ACTION_SEARCH_ZERO_STATE";
W[W.LATENCY_ACTION_LIVE_PAGINATION]="LATENCY_ACTION_LIVE_PAGINATION";W[W.LATENCY_ACTION_LIVE]="LATENCY_ACTION_LIVE";W[W.LATENCY_ACTION_PREBUFFER]="LATENCY_ACTION_PREBUFFER";W[W.LATENCY_ACTION_TENX]="LATENCY_ACTION_TENX";W[W.LATENCY_ACTION_KIDS_PROFILE_SETTINGS]="LATENCY_ACTION_KIDS_PROFILE_SETTINGS";W[W.LATENCY_ACTION_KIDS_WATCH_IT_AGAIN]="LATENCY_ACTION_KIDS_WATCH_IT_AGAIN";W[W.LATENCY_ACTION_KIDS_SECRET_CODE]="LATENCY_ACTION_KIDS_SECRET_CODE";W[W.LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS]="LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS";
W[W.LATENCY_ACTION_KIDS_ONBOARDING]="LATENCY_ACTION_KIDS_ONBOARDING";W[W.LATENCY_ACTION_KIDS_VOICE_SEARCH]="LATENCY_ACTION_KIDS_VOICE_SEARCH";W[W.LATENCY_ACTION_KIDS_CURATED_COLLECTION]="LATENCY_ACTION_KIDS_CURATED_COLLECTION";W[W.LATENCY_ACTION_KIDS_LIBRARY]="LATENCY_ACTION_KIDS_LIBRARY";W[W.LATENCY_ACTION_CREATOR_PROMOTION_LIST]="LATENCY_ACTION_CREATOR_PROMOTION_LIST";W[W.LATENCY_ACTION_CREATOR_PROMOTION_EDIT]="LATENCY_ACTION_CREATOR_PROMOTION_EDIT";
W[W.LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS]="LATENCY_ACTION_CREATOR_VIDEO_TRANSLATIONS";W[W.LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION]="LATENCY_ACTION_CREATOR_VIDEO_MONETIZATION";W[W.LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_STREAMING";W[W.LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS]="LATENCY_ACTION_CREATOR_VIDEO_LIVE_SETTINGS";W[W.LATENCY_ACTION_CREATOR_VIDEO_EDITOR_ASYNC]="LATENCY_ACTION_CREATOR_VIDEO_EDITOR_ASYNC";
W[W.LATENCY_ACTION_CREATOR_VIDEO_EDITOR]="LATENCY_ACTION_CREATOR_VIDEO_EDITOR";W[W.LATENCY_ACTION_CREATOR_VIDEO_EDIT]="LATENCY_ACTION_CREATOR_VIDEO_EDIT";W[W.LATENCY_ACTION_CREATOR_VIDEO_COMMENTS]="LATENCY_ACTION_CREATOR_VIDEO_COMMENTS";W[W.LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS]="LATENCY_ACTION_CREATOR_VIDEO_ANALYTICS";W[W.LATENCY_ACTION_CREATOR_SONG_ANALYTICS]="LATENCY_ACTION_CREATOR_SONG_ANALYTICS";W[W.LATENCY_ACTION_CREATOR_POST_LIST]="LATENCY_ACTION_CREATOR_POST_LIST";
W[W.LATENCY_ACTION_CREATOR_POST_EDIT]="LATENCY_ACTION_CREATOR_POST_EDIT";W[W.LATENCY_ACTION_CREATOR_POST_COMMENTS]="LATENCY_ACTION_CREATOR_POST_COMMENTS";W[W.LATENCY_ACTION_CREATOR_LIVE_STREAMING]="LATENCY_ACTION_CREATOR_LIVE_STREAMING";W[W.LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT]="LATENCY_ACTION_CREATOR_DIALOG_VIDEO_COPYRIGHT";W[W.LATENCY_ACTION_CREATOR_DIALOG_UPLOADS]="LATENCY_ACTION_CREATOR_DIALOG_UPLOADS";W[W.LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES]="LATENCY_ACTION_CREATOR_DIALOG_COPYRIGHT_STRIKES";
W[W.LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS]="LATENCY_ACTION_CREATOR_CHANNEL_VIDEOS";W[W.LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS]="LATENCY_ACTION_CREATOR_CHANNEL_TRANSLATIONS";W[W.LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS]="LATENCY_ACTION_CREATOR_CHANNEL_PLAYLISTS";W[W.LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC_STOREFRONT";W[W.LATENCY_ACTION_CREATOR_CHANNEL_MUSIC]="LATENCY_ACTION_CREATOR_CHANNEL_MUSIC";W[W.LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION]="LATENCY_ACTION_CREATOR_CHANNEL_MONETIZATION";
W[W.LATENCY_ACTION_CREATOR_CHANNEL_EDITING]="LATENCY_ACTION_CREATOR_CHANNEL_EDITING";W[W.LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD]="LATENCY_ACTION_CREATOR_CHANNEL_DASHBOARD";W[W.LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT]="LATENCY_ACTION_CREATOR_CHANNEL_COPYRIGHT";W[W.LATENCY_ACTION_CREATOR_CMS_VIDEOS]="LATENCY_ACTION_CREATOR_CMS_VIDEOS";W[W.LATENCY_ACTION_CREATOR_CMS_REPORTS]="LATENCY_ACTION_CREATOR_CMS_REPORTS";W[W.LATENCY_ACTION_CREATOR_CMS_ISSUES]="LATENCY_ACTION_CREATOR_CMS_ISSUES";
W[W.LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING]="LATENCY_ACTION_CREATOR_CMS_MANUAL_CLAIMING";W[W.LATENCY_ACTION_CREATOR_CMS_DASHBOARD]="LATENCY_ACTION_CREATOR_CMS_DASHBOARD";W[W.LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY]="LATENCY_ACTION_CREATOR_CMS_CONTENT_DELIVERY";W[W.LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS]="LATENCY_ACTION_CREATOR_CMS_CLAIMED_VIDEOS";W[W.LATENCY_ACTION_CREATOR_CMS_CHANNELS]="LATENCY_ACTION_CREATOR_CMS_CHANNELS";W[W.LATENCY_ACTION_CREATOR_CMS_ASSETS]="LATENCY_ACTION_CREATOR_CMS_ASSETS";
W[W.LATENCY_ACTION_CREATOR_CMS_ANALYTICS]="LATENCY_ACTION_CREATOR_CMS_ANALYTICS";W[W.LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS]="LATENCY_ACTION_CREATOR_CHANNEL_COMMENTS";W[W.LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS]="LATENCY_ACTION_CREATOR_CHANNEL_ANALYTICS";W[W.LATENCY_ACTION_CREATOR_ARTIST_PROFILE]="LATENCY_ACTION_CREATOR_ARTIST_PROFILE";W[W.LATENCY_ACTION_CREATOR_ARTIST_CONCERTS]="LATENCY_ACTION_CREATOR_ARTIST_CONCERTS";W[W.LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS]="LATENCY_ACTION_CREATOR_ARTIST_ANALYTICS";
W[W.LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE]="LATENCY_ACTION_CREATOR_ANALYTICS_EXPLORE";W[W.LATENCY_ACTION_EXPERIMENTAL_WATCH_UI]="LATENCY_ACTION_EXPERIMENTAL_WATCH_UI";W[W.LATENCY_ACTION_STORYBOARD_THUMBNAILS]="LATENCY_ACTION_STORYBOARD_THUMBNAILS";W[W.LATENCY_ACTION_SEARCH_THUMBNAILS]="LATENCY_ACTION_SEARCH_THUMBNAILS";W[W.LATENCY_ACTION_ON_DEVICE_MODEL_DOWNLOAD]="LATENCY_ACTION_ON_DEVICE_MODEL_DOWNLOAD";W[W.LATENCY_ACTION_VOICE_ASSISTANT]="LATENCY_ACTION_VOICE_ASSISTANT";
W[W.LATENCY_ACTION_SEARCH_UI]="LATENCY_ACTION_SEARCH_UI";W[W.LATENCY_ACTION_SUGGEST]="LATENCY_ACTION_SUGGEST";W[W.LATENCY_ACTION_AUTO_SEARCH]="LATENCY_ACTION_AUTO_SEARCH";W[W.LATENCY_ACTION_DOWNLOADS]="LATENCY_ACTION_DOWNLOADS";W[W.LATENCY_ACTION_EXPLORE]="LATENCY_ACTION_EXPLORE";W[W.LATENCY_ACTION_VIDEO_LIST]="LATENCY_ACTION_VIDEO_LIST";W[W.LATENCY_ACTION_HOME_RESUME]="LATENCY_ACTION_HOME_RESUME";W[W.LATENCY_ACTION_SUBSCRIPTIONS_LIST]="LATENCY_ACTION_SUBSCRIPTIONS_LIST";
W[W.LATENCY_ACTION_THUMBNAIL_LOAD]="LATENCY_ACTION_THUMBNAIL_LOAD";W[W.LATENCY_ACTION_FIRST_THUMBNAIL_LOAD]="LATENCY_ACTION_FIRST_THUMBNAIL_LOAD";W[W.LATENCY_ACTION_SUBSCRIPTIONS_FEED]="LATENCY_ACTION_SUBSCRIPTIONS_FEED";W[W.LATENCY_ACTION_SUBSCRIPTIONS]="LATENCY_ACTION_SUBSCRIPTIONS";W[W.LATENCY_ACTION_TRENDING]="LATENCY_ACTION_TRENDING";W[W.LATENCY_ACTION_LIBRARY]="LATENCY_ACTION_LIBRARY";W[W.LATENCY_ACTION_VIDEO_THUMBNAIL]="LATENCY_ACTION_VIDEO_THUMBNAIL";W[W.LATENCY_ACTION_SHOW_MORE]="LATENCY_ACTION_SHOW_MORE";
W[W.LATENCY_ACTION_VIDEO_PREVIEW]="LATENCY_ACTION_VIDEO_PREVIEW";W[W.LATENCY_ACTION_AD_TO_AD]="LATENCY_ACTION_AD_TO_AD";W[W.LATENCY_ACTION_VIDEO_TO_AD]="LATENCY_ACTION_VIDEO_TO_AD";W[W.LATENCY_ACTION_AD_TO_VIDEO]="LATENCY_ACTION_AD_TO_VIDEO";W[W.LATENCY_ACTION_DIRECT_PLAYBACK]="LATENCY_ACTION_DIRECT_PLAYBACK";W[W.LATENCY_ACTION_PREBUFFER_VIDEO]="LATENCY_ACTION_PREBUFFER_VIDEO";W[W.LATENCY_ACTION_PREFETCH_VIDEO]="LATENCY_ACTION_PREFETCH_VIDEO";W[W.LATENCY_ACTION_STARTUP]="LATENCY_ACTION_STARTUP";
W[W.LATENCY_ACTION_ONBOARDING]="LATENCY_ACTION_ONBOARDING";W[W.LATENCY_ACTION_LOGIN]="LATENCY_ACTION_LOGIN";W[W.LATENCY_ACTION_REEL_WATCH]="LATENCY_ACTION_REEL_WATCH";W[W.LATENCY_ACTION_WATCH]="LATENCY_ACTION_WATCH";W[W.LATENCY_ACTION_RESULTS]="LATENCY_ACTION_RESULTS";W[W.LATENCY_ACTION_CHANNELS]="LATENCY_ACTION_CHANNELS";W[W.LATENCY_ACTION_HOME]="LATENCY_ACTION_HOME";W[W.LATENCY_ACTION_BROWSE]="LATENCY_ACTION_BROWSE";W[W.LATENCY_ACTION_USER_ACTION]="LATENCY_ACTION_USER_ACTION";
W[W.LATENCY_ACTION_INFRASTRUCTURE]="LATENCY_ACTION_INFRASTRUCTURE";W[W.LATENCY_ACTION_PAGE_NAVIGATION]="LATENCY_ACTION_PAGE_NAVIGATION";W[W.LATENCY_ACTION_UNKNOWN]="LATENCY_ACTION_UNKNOWN";var ru={LATENCY_NETWORK_MOBILE:2,LATENCY_NETWORK_WIFI:1,LATENCY_NETWORK_UNKNOWN:0};ru[ru.LATENCY_NETWORK_MOBILE]="LATENCY_NETWORK_MOBILE";ru[ru.LATENCY_NETWORK_WIFI]="LATENCY_NETWORK_WIFI";ru[ru.LATENCY_NETWORK_UNKNOWN]="LATENCY_NETWORK_UNKNOWN";
var X={CONN_INVALID:31,CONN_CELLULAR_5G_NSA:12,CONN_CELLULAR_5G_SA:11,CONN_WIFI_METERED:10,CONN_CELLULAR_5G:9,CONN_DISCO:8,CONN_CELLULAR_UNKNOWN:7,CONN_CELLULAR_4G:6,CONN_CELLULAR_3G:5,CONN_CELLULAR_2G:4,CONN_WIFI:3,CONN_NONE:2,CONN_UNKNOWN:1,CONN_DEFAULT:0};X[X.CONN_INVALID]="CONN_INVALID";X[X.CONN_CELLULAR_5G_NSA]="CONN_CELLULAR_5G_NSA";X[X.CONN_CELLULAR_5G_SA]="CONN_CELLULAR_5G_SA";X[X.CONN_WIFI_METERED]="CONN_WIFI_METERED";X[X.CONN_CELLULAR_5G]="CONN_CELLULAR_5G";X[X.CONN_DISCO]="CONN_DISCO";
X[X.CONN_CELLULAR_UNKNOWN]="CONN_CELLULAR_UNKNOWN";X[X.CONN_CELLULAR_4G]="CONN_CELLULAR_4G";X[X.CONN_CELLULAR_3G]="CONN_CELLULAR_3G";X[X.CONN_CELLULAR_2G]="CONN_CELLULAR_2G";X[X.CONN_WIFI]="CONN_WIFI";X[X.CONN_NONE]="CONN_NONE";X[X.CONN_UNKNOWN]="CONN_UNKNOWN";X[X.CONN_DEFAULT]="CONN_DEFAULT";
var Y={DETAILED_NETWORK_TYPE_NR_NSA:126,DETAILED_NETWORK_TYPE_NR_SA:125,DETAILED_NETWORK_TYPE_INTERNAL_WIFI_IMPAIRED:124,DETAILED_NETWORK_TYPE_APP_WIFI_HOTSPOT:123,DETAILED_NETWORK_TYPE_DISCONNECTED:122,DETAILED_NETWORK_TYPE_NON_MOBILE_UNKNOWN:121,DETAILED_NETWORK_TYPE_MOBILE_UNKNOWN:120,DETAILED_NETWORK_TYPE_WIMAX:119,DETAILED_NETWORK_TYPE_ETHERNET:118,DETAILED_NETWORK_TYPE_BLUETOOTH:117,DETAILED_NETWORK_TYPE_WIFI:116,DETAILED_NETWORK_TYPE_LTE:115,DETAILED_NETWORK_TYPE_HSPAP:114,DETAILED_NETWORK_TYPE_EHRPD:113,
DETAILED_NETWORK_TYPE_EVDO_B:112,DETAILED_NETWORK_TYPE_UMTS:111,DETAILED_NETWORK_TYPE_IDEN:110,DETAILED_NETWORK_TYPE_HSUPA:109,DETAILED_NETWORK_TYPE_HSPA:108,DETAILED_NETWORK_TYPE_HSDPA:107,DETAILED_NETWORK_TYPE_EVDO_A:106,DETAILED_NETWORK_TYPE_EVDO_0:105,DETAILED_NETWORK_TYPE_CDMA:104,DETAILED_NETWORK_TYPE_1_X_RTT:103,DETAILED_NETWORK_TYPE_GPRS:102,DETAILED_NETWORK_TYPE_EDGE:101,DETAILED_NETWORK_TYPE_UNKNOWN:0};Y[Y.DETAILED_NETWORK_TYPE_NR_NSA]="DETAILED_NETWORK_TYPE_NR_NSA";
Y[Y.DETAILED_NETWORK_TYPE_NR_SA]="DETAILED_NETWORK_TYPE_NR_SA";Y[Y.DETAILED_NETWORK_TYPE_INTERNAL_WIFI_IMPAIRED]="DETAILED_NETWORK_TYPE_INTERNAL_WIFI_IMPAIRED";Y[Y.DETAILED_NETWORK_TYPE_APP_WIFI_HOTSPOT]="DETAILED_NETWORK_TYPE_APP_WIFI_HOTSPOT";Y[Y.DETAILED_NETWORK_TYPE_DISCONNECTED]="DETAILED_NETWORK_TYPE_DISCONNECTED";Y[Y.DETAILED_NETWORK_TYPE_NON_MOBILE_UNKNOWN]="DETAILED_NETWORK_TYPE_NON_MOBILE_UNKNOWN";Y[Y.DETAILED_NETWORK_TYPE_MOBILE_UNKNOWN]="DETAILED_NETWORK_TYPE_MOBILE_UNKNOWN";
Y[Y.DETAILED_NETWORK_TYPE_WIMAX]="DETAILED_NETWORK_TYPE_WIMAX";Y[Y.DETAILED_NETWORK_TYPE_ETHERNET]="DETAILED_NETWORK_TYPE_ETHERNET";Y[Y.DETAILED_NETWORK_TYPE_BLUETOOTH]="DETAILED_NETWORK_TYPE_BLUETOOTH";Y[Y.DETAILED_NETWORK_TYPE_WIFI]="DETAILED_NETWORK_TYPE_WIFI";Y[Y.DETAILED_NETWORK_TYPE_LTE]="DETAILED_NETWORK_TYPE_LTE";Y[Y.DETAILED_NETWORK_TYPE_HSPAP]="DETAILED_NETWORK_TYPE_HSPAP";Y[Y.DETAILED_NETWORK_TYPE_EHRPD]="DETAILED_NETWORK_TYPE_EHRPD";Y[Y.DETAILED_NETWORK_TYPE_EVDO_B]="DETAILED_NETWORK_TYPE_EVDO_B";
Y[Y.DETAILED_NETWORK_TYPE_UMTS]="DETAILED_NETWORK_TYPE_UMTS";Y[Y.DETAILED_NETWORK_TYPE_IDEN]="DETAILED_NETWORK_TYPE_IDEN";Y[Y.DETAILED_NETWORK_TYPE_HSUPA]="DETAILED_NETWORK_TYPE_HSUPA";Y[Y.DETAILED_NETWORK_TYPE_HSPA]="DETAILED_NETWORK_TYPE_HSPA";Y[Y.DETAILED_NETWORK_TYPE_HSDPA]="DETAILED_NETWORK_TYPE_HSDPA";Y[Y.DETAILED_NETWORK_TYPE_EVDO_A]="DETAILED_NETWORK_TYPE_EVDO_A";Y[Y.DETAILED_NETWORK_TYPE_EVDO_0]="DETAILED_NETWORK_TYPE_EVDO_0";Y[Y.DETAILED_NETWORK_TYPE_CDMA]="DETAILED_NETWORK_TYPE_CDMA";
Y[Y.DETAILED_NETWORK_TYPE_1_X_RTT]="DETAILED_NETWORK_TYPE_1_X_RTT";Y[Y.DETAILED_NETWORK_TYPE_GPRS]="DETAILED_NETWORK_TYPE_GPRS";Y[Y.DETAILED_NETWORK_TYPE_EDGE]="DETAILED_NETWORK_TYPE_EDGE";Y[Y.DETAILED_NETWORK_TYPE_UNKNOWN]="DETAILED_NETWORK_TYPE_UNKNOWN";var su={LATENCY_PLAYER_RTSP:7,LATENCY_PLAYER_HTML5_INLINE:6,LATENCY_PLAYER_HTML5_FULLSCREEN:5,LATENCY_PLAYER_HTML5:4,LATENCY_PLAYER_FRAMEWORK:3,LATENCY_PLAYER_FLASH:2,LATENCY_PLAYER_EXO:1,LATENCY_PLAYER_UNKNOWN:0};su[su.LATENCY_PLAYER_RTSP]="LATENCY_PLAYER_RTSP";
su[su.LATENCY_PLAYER_HTML5_INLINE]="LATENCY_PLAYER_HTML5_INLINE";su[su.LATENCY_PLAYER_HTML5_FULLSCREEN]="LATENCY_PLAYER_HTML5_FULLSCREEN";su[su.LATENCY_PLAYER_HTML5]="LATENCY_PLAYER_HTML5";su[su.LATENCY_PLAYER_FRAMEWORK]="LATENCY_PLAYER_FRAMEWORK";su[su.LATENCY_PLAYER_FLASH]="LATENCY_PLAYER_FLASH";su[su.LATENCY_PLAYER_EXO]="LATENCY_PLAYER_EXO";su[su.LATENCY_PLAYER_UNKNOWN]="LATENCY_PLAYER_UNKNOWN";
var tu={LATENCY_AD_BREAK_TYPE_POSTROLL:3,LATENCY_AD_BREAK_TYPE_MIDROLL:2,LATENCY_AD_BREAK_TYPE_PREROLL:1,LATENCY_AD_BREAK_TYPE_UNKNOWN:0};tu[tu.LATENCY_AD_BREAK_TYPE_POSTROLL]="LATENCY_AD_BREAK_TYPE_POSTROLL";tu[tu.LATENCY_AD_BREAK_TYPE_MIDROLL]="LATENCY_AD_BREAK_TYPE_MIDROLL";tu[tu.LATENCY_AD_BREAK_TYPE_PREROLL]="LATENCY_AD_BREAK_TYPE_PREROLL";tu[tu.LATENCY_AD_BREAK_TYPE_UNKNOWN]="LATENCY_AD_BREAK_TYPE_UNKNOWN";var uu={LATENCY_ACTION_ERROR_STARTUP_TIMEOUT:1,LATENCY_ACTION_ERROR_UNSPECIFIED:0};
uu[uu.LATENCY_ACTION_ERROR_STARTUP_TIMEOUT]="LATENCY_ACTION_ERROR_STARTUP_TIMEOUT";uu[uu.LATENCY_ACTION_ERROR_UNSPECIFIED]="LATENCY_ACTION_ERROR_UNSPECIFIED";var vu={LIVE_STREAM_MODE_WINDOW:5,LIVE_STREAM_MODE_POST:4,LIVE_STREAM_MODE_LP:3,LIVE_STREAM_MODE_LIVE:2,LIVE_STREAM_MODE_DVR:1,LIVE_STREAM_MODE_UNKNOWN:0};vu[vu.LIVE_STREAM_MODE_WINDOW]="LIVE_STREAM_MODE_WINDOW";vu[vu.LIVE_STREAM_MODE_POST]="LIVE_STREAM_MODE_POST";vu[vu.LIVE_STREAM_MODE_LP]="LIVE_STREAM_MODE_LP";
vu[vu.LIVE_STREAM_MODE_LIVE]="LIVE_STREAM_MODE_LIVE";vu[vu.LIVE_STREAM_MODE_DVR]="LIVE_STREAM_MODE_DVR";vu[vu.LIVE_STREAM_MODE_UNKNOWN]="LIVE_STREAM_MODE_UNKNOWN";var wu={VIDEO_STREAM_TYPE_VOD:3,VIDEO_STREAM_TYPE_DVR:2,VIDEO_STREAM_TYPE_LIVE:1,VIDEO_STREAM_TYPE_UNSPECIFIED:0};wu[wu.VIDEO_STREAM_TYPE_VOD]="VIDEO_STREAM_TYPE_VOD";wu[wu.VIDEO_STREAM_TYPE_DVR]="VIDEO_STREAM_TYPE_DVR";wu[wu.VIDEO_STREAM_TYPE_LIVE]="VIDEO_STREAM_TYPE_LIVE";wu[wu.VIDEO_STREAM_TYPE_UNSPECIFIED]="VIDEO_STREAM_TYPE_UNSPECIFIED";
var xu={YT_IDB_TRANSACTION_TYPE_READ:2,YT_IDB_TRANSACTION_TYPE_WRITE:1,YT_IDB_TRANSACTION_TYPE_UNKNOWN:0};xu[xu.YT_IDB_TRANSACTION_TYPE_READ]="YT_IDB_TRANSACTION_TYPE_READ";xu[xu.YT_IDB_TRANSACTION_TYPE_WRITE]="YT_IDB_TRANSACTION_TYPE_WRITE";xu[xu.YT_IDB_TRANSACTION_TYPE_UNKNOWN]="YT_IDB_TRANSACTION_TYPE_UNKNOWN";var yu={PLAYER_ROTATION_TYPE_PORTRAIT_TO_FULLSCREEN:2,PLAYER_ROTATION_TYPE_FULLSCREEN_TO_PORTRAIT:1,PLAYER_ROTATION_TYPE_UNKNOWN:0};yu[yu.PLAYER_ROTATION_TYPE_PORTRAIT_TO_FULLSCREEN]="PLAYER_ROTATION_TYPE_PORTRAIT_TO_FULLSCREEN";
yu[yu.PLAYER_ROTATION_TYPE_FULLSCREEN_TO_PORTRAIT]="PLAYER_ROTATION_TYPE_FULLSCREEN_TO_PORTRAIT";yu[yu.PLAYER_ROTATION_TYPE_UNKNOWN]="PLAYER_ROTATION_TYPE_UNKNOWN";var zu="actionVisualElement spinnerInfo resourceInfo playerInfo commentInfo mdxInfo watchInfo thumbnailLoadInfo creatorInfo unpluggedInfo reelInfo subscriptionsFeedInfo requestIds mediaBrowserActionInfo musicLoadActionInfo shoppingInfo webViewInfo prefetchInfo accelerationSession commerceInfo webInfo tvInfo kabukiInfo mwebInfo musicInfo".split(" ");var Au=y.ytLoggingLatencyUsageStats_||{};z("ytLoggingLatencyUsageStats_",Au);function Bu(){this.h=0}
function Cu(){Bu.h||(Bu.h=new Bu);return Bu.h}
Bu.prototype.tick=function(a,b,c,d){Du(this,"tick_"+a+"_"+b)||(c={timestamp:c,cttAuthInfo:d},M("web_csi_via_jspb")?(d=new ck,D(d,1,a),D(d,2,b),a=new fk,be(a,ck,5,gk,d),gs(a,c)):Em("latencyActionTicked",{tickName:a,clientActionNonce:b},c))};
Bu.prototype.info=function(a,b,c){var d=Object.keys(a).join("");Du(this,"info_"+d+"_"+b)||(a=Object.assign({},a),a.clientActionNonce=b,Em("latencyActionInfo",a,{cttAuthInfo:c}))};
Bu.prototype.jspbInfo=function(a,b,c){for(var d="",e=0;e<a.toJSON().length;e++)void 0!==a.toJSON()[e]&&(d=0===e?d.concat(""+e):d.concat("_"+e));Du(this,"info_"+d+"_"+b)||(D(a,2,b),b={cttAuthInfo:c},c=new fk,be(c,Yj,7,gk,a),gs(c,b))};
Bu.prototype.span=function(a,b,c){var d=Object.keys(a).join("");Du(this,"span_"+d+"_"+b)||(a.clientActionNonce=b,Em("latencyActionSpan",a,{cttAuthInfo:c}))};
function Du(a,b){Au[b]=Au[b]||{count:0};var c=Au[b];c.count++;c.time=Q();a.h||(a.h=nm(function(){var d=Q(),e;for(e in Au)Au[e]&&6E4<d-Au[e].time&&delete Au[e];a&&(a.h=0)},5E3));
return 5<c.count?(6===c.count&&1>1E5*Math.random()&&(c=new P("CSI data exceeded logging limit with key",b.split("_")),0<=b.indexOf("plev")||us(c)),!0):!1}
;function Eu(){var a=["ol"];iu("").info.actionType="embed";a&&Rk("TIMING_AFT_KEYS",a);Rk("TIMING_ACTION","embed");if(M("web_csi_via_jspb")){a=L("TIMING_INFO",{});var b=new Yj;a=p(Object.entries(a));for(var c=a.next();!c.done;c=a.next()){var d=p(c.value);c=d.next().value;d=d.next().value;switch(c){case "GetBrowse_rid":var e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetGuide_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetHome_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);
break;case "GetPlayer_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetSearch_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetSettings_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetTrending_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "GetWatchNext_rid":e=new bk;D(e,1,c);D(e,2,String(d));ak(b,e);break;case "yt_red":D(b,14,!!d);break;case "yt_ad":D(b,9,!!d)}}Fu(b);b=new Yj;b=D(b,25,!0);b=D(b,1,W[pu(L("TIMING_ACTION"))]);(a=L("PREVIOUS_ACTION"))&&
D(b,13,W[pu(a)]);(a=L("CLIENT_PROTOCOL"))&&D(b,33,a);(a=L("CLIENT_TRANSPORT"))&&D(b,34,a);(a=Ms())&&"UNDEFINED_CSN"!==a&&D(b,4,a);a=Gu();1!==a&&-1!==a||D(b,6,!0);a=Zt();M("skip_setting_info_in_csi_data_object")&&$t();D(b,3,"cold");Hu(a);a=Iu();if(0<a.length)for(a=p(a),c=a.next();!c.done;c=a.next())c=c.value,d=new Xj,D(d,1,c),de(b,83,Xj,d);Fu(b)}else{a=L("TIMING_INFO",{});for(b in a)a.hasOwnProperty(b)&&Ju(b,a[b]);b={isNavigation:!0,actionType:pu(L("TIMING_ACTION"))};if(a=L("PREVIOUS_ACTION"))b.previousAction=
pu(a);if(a=L("CLIENT_PROTOCOL"))b.httpProtocol=a;if(a=L("CLIENT_TRANSPORT"))b.transportProtocol=a;(a=Ms())&&"UNDEFINED_CSN"!==a&&(b.clientScreenNonce=a);a=Gu();if(1===a||-1===a)b.isVisible=!0;M("skip_setting_info_in_csi_data_object")&&$t();Zt();b.loadType="cold";Hu(Zt());a=Iu();if(0<a.length)for(b.resourceInfo=[],a=p(a),c=a.next();!c.done;c=a.next())b.resourceInfo.push({resourceCache:c.value});Ku(b)}b=Zt();a=cu();if(!(M("skip_setting_info_in_csi_data_object")&&"cold"!==$t().loadType||"cold"!==b.yt_lt&&
"cold"!==a.loadType)){c=au();d=bu();d=d.gelTicks?d.gelTicks:d.gelTicks={};for(var f in c)if(!(f in d))if("number"===typeof c[f])Z(f,Ut(f));else if(M("log_repeated_ytcsi_ticks")){e=p(c[f]);for(var g=e.next();!g.done;g=e.next())Z(f.slice(1),g.value)}f={};c=!1;d=p(Object.keys(b));for(e=d.next();!e.done;e=d.next())e=e.value,(e=qu(e,b[e]))&&!fu(cu(),e)&&(It(a,e),It(f,e),c=!0);c&&Ku(f)}z("ytglobal.timingready_",!0);f=L("TIMING_ACTION");B("ytglobal.timingready_")&&f&&"_start"in au()&&Tt()&&eu()}
function Ju(a,b,c,d){if(null!==b){var e=Zt(c);M("skip_setting_info_in_csi_data_object")?"yt_lt"===a&&(e="string"===typeof b?b:""+b,$t(c).loadType=e):e[a]=b;(a=qu(a,b,c))&&Ku(a,c,d)}}
function Ku(a,b,c){if(!M("web_csi_via_jspb")||(void 0===c?0:c))c=iu(b||""),It(c.info,a),M("skip_setting_info_in_csi_data_object")&&a.loadType&&(c=a.loadType,$t(b).loadType=c),It(cu(b),a),c=du(b),b=Yt(b).cttAuthInfo,Cu().info(a,c,b);else{c=new Yj;var d=Object.keys(a);a=Object.values(a);for(var e=0;e<d.length;e++){var f=d[e];try{switch(f){case "actionType":D(c,1,W[a[e]]);break;case "clientActionNonce":D(c,2,a[e]);break;case "clientScreenNonce":D(c,4,a[e]);break;case "loadType":D(c,3,a[e]);break;case "isPrewarmedLaunch":D(c,
92,a[e]);break;case "isFirstInstall":D(c,55,a[e]);break;case "networkType":D(c,5,ru[a[e]]);break;case "connectionType":D(c,26,X[a[e]]);break;case "detailedConnectionType":D(c,27,Y[a[e]]);break;case "isVisible":D(c,6,a[e]);break;case "playerType":D(c,7,su[a[e]]);break;case "clientPlaybackNonce":D(c,8,a[e]);break;case "adClientPlaybackNonce":D(c,28,a[e]);break;case "previousCpn":D(c,77,a[e]);break;case "targetCpn":D(c,76,a[e]);break;case "isMonetized":D(c,9,a[e]);break;case "isPrerollAllowed":D(c,16,
a[e]);break;case "isPrerollShown":D(c,17,a[e]);break;case "adType":D(c,12,a[e]);break;case "adTypesAllowed":D(c,36,a[e]);break;case "adNetworks":D(c,37,a[e]);break;case "previousAction":D(c,13,W[a[e]]);break;case "isRedSubscriber":D(c,14,a[e]);break;case "serverTimeMs":D(c,15,a[e]);break;case "videoId":c.setVideoId(a[e]);break;case "adVideoId":D(c,20,a[e]);break;case "targetVideoId":D(c,78,a[e]);break;case "adBreakType":D(c,21,tu[a[e]]);break;case "isNavigation":D(c,25,a[e]);break;case "viewportHeight":D(c,
29,a[e]);break;case "viewportWidth":D(c,30,a[e]);break;case "screenHeight":D(c,84,a[e]);break;case "screenWidth":D(c,85,a[e]);break;case "browseId":D(c,31,a[e]);break;case "isCacheHit":D(c,32,a[e]);break;case "httpProtocol":D(c,33,a[e]);break;case "transportProtocol":D(c,34,a[e]);break;case "searchQuery":D(c,41,a[e]);break;case "isContinuation":D(c,42,a[e]);break;case "availableProcessors":D(c,43,a[e]);break;case "sdk":D(c,44,a[e]);break;case "isLocalStream":D(c,45,a[e]);break;case "navigationRequestedSameUrl":D(c,
64,a[e]);break;case "shellStartupDurationMs":D(c,70,a[e]);break;case "appInstallDataAgeMs":D(c,73,a[e]);break;case "latencyActionError":D(c,71,uu[a[e]]);break;case "actionStep":D(c,79,a[e]);break;case "jsHeapSizeLimit":D(c,80,a[e]);break;case "totalJsHeapSize":D(c,81,a[e]);break;case "usedJsHeapSize":D(c,82,a[e]);break;case "sourceVideoDurationMs":D(c,90,a[e]);break;case "videoOutputFrames":D(c,93,a[e]);break;case "isResume":D(c,104,a[e]);break;case "debugTicksExcluded":D(c,105,a[e]);break;case "adPrebufferedTimeSecs":D(c,
39,a[e]);break;case "isLivestream":D(c,47,a[e]);break;case "liveStreamMode":D(c,91,vu[a[e]]);break;case "adCpn2":D(c,48,a[e]);break;case "adDaiDriftMillis":D(c,49,a[e]);break;case "videoStreamType":D(c,53,wu[a[e]]);break;case "playbackRequiresTap":D(c,56,a[e]);break;case "performanceNavigationTiming":D(c,67,a[e]);break;case "transactionType":D(c,74,xu[a[e]]);break;case "playerRotationType":D(c,101,yu[a[e]]);break;case "allowedPreroll":D(c,10,a[e]);break;case "shownPreroll":D(c,11,a[e]);break;case "getHomeRequestId":D(c,
57,a[e]);break;case "getSearchRequestId":D(c,60,a[e]);break;case "getPlayerRequestId":D(c,61,a[e]);break;case "getWatchNextRequestId":D(c,62,a[e]);break;case "getBrowseRequestId":D(c,63,a[e]);break;case "getLibraryRequestId":D(c,66,a[e]);break;default:zu.includes(f)&&cl(new P("Codegen laipb translator asked to translate message field",""+f))}}catch(g){cl(Error("Codegen laipb translator failed to set "+f))}}Fu(c,b)}}
function Fu(a,b){if(M("skip_setting_info_in_csi_data_object")){var c=fe(Sd(a,3),"");c&&($t(b).loadType=c)}else c=bu(b),c.jspbInfos||(c.jspbInfos=[]),c.jspbInfos.push(le(a));iu(b||"").jspbInfo.push(a);c=du(b);b=Yt(b).cttAuthInfo;Cu().jspbInfo(a,c,b)}
function Z(a,b,c){if(!b&&"_"!==a[0]){var d=a;S.mark&&(0==d.lastIndexOf("mark_",0)||(d="mark_"+d),c&&(d+=" ("+c+")"),S.mark(d))}d=iu(c||"");d.tick[a]=b||Q();if(d.callback&&d.callback[a]){d=p(d.callback[a]);for(var e=d.next();!e.done;e=d.next())e=e.value,e()}d=bu(c);d.gelTicks&&(d.gelTicks[a]=!0);e=au(c);d=b||Q();M("log_repeated_ytcsi_ticks")?a in e||(e[a]=d):e[a]=d;e=du(c);var f=Yt(c).cttAuthInfo;"_start"===a?(a=Cu(),Du(a,"baseline_"+e)||(b={timestamp:b,cttAuthInfo:f},M("web_csi_via_jspb")?(a=new Wj,
D(a,1,e),e=new fk,be(e,Wj,6,gk,a),gs(e,b)):Em("latencyActionBaselined",{clientActionNonce:e},b))):Cu().tick(a,e,b,f);eu(c);return d}
function Lu(){var a=du();requestAnimationFrame(function(){setTimeout(function(){a===du()&&Z("ol",void 0,void 0)},0)})}
function Gu(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=Bq+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function Hu(a){var b=Vt(),c=Xt(),d=L("CSI_START_TIMESTAMP_MILLIS",0);0<d&&!M("embeds_web_enable_csi_start_override_killswitch")&&(c=d);c&&(Z("srt",b.responseStart),1!==a.prerender&&Z("_start",c,void 0));a=gu();0<a&&Z("fpt",a);a=Vt();a.isPerformanceNavigationTiming&&Ku({performanceNavigationTiming:!0});Z("nreqs",a.requestStart,void 0);Z("nress",a.responseStart,void 0);Z("nrese",a.responseEnd,void 0);0<a.redirectEnd-a.redirectStart&&(Z("nrs",a.redirectStart,void 0),Z("nre",a.redirectEnd,void 0));0<
a.domainLookupEnd-a.domainLookupStart&&(Z("ndnss",a.domainLookupStart,void 0),Z("ndnse",a.domainLookupEnd,void 0));0<a.connectEnd-a.connectStart&&(Z("ntcps",a.connectStart,void 0),Z("ntcpe",a.connectEnd,void 0));a.secureConnectionStart>=Xt()&&0<a.connectEnd-a.secureConnectionStart&&(Z("nstcps",a.secureConnectionStart,void 0),Z("ntcpe",a.connectEnd,void 0));S&&"getEntriesByType"in S&&Mu()}
function Nu(a,b){a=document.querySelector(a);if(!a)return!1;var c="",d=a.nodeName;"SCRIPT"===d?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):"LINK"===d&&(c=a.href);jc()&&a.setAttribute("nonce",jc());return c?(a=S.getEntriesByName(c))&&a[0]&&(a=a[0],c=Xt(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),void 0!==a.transferSize&&0===a.transferSize)?!0:!1:!1}
function Iu(){var a=[];if(document.querySelector&&S&&S.getEntriesByName)for(var b in St)if(St.hasOwnProperty(b)){var c=St[b];Nu(b,c)&&a.push(c)}return a}
function Mu(){var a=window.location.protocol,b=S.getEntriesByType("resource");b=ib(b,function(c){return 0===c.name.indexOf(a+"//fonts.gstatic.com/s/")});
(b=kb(b,function(c,d){return d.duration>c.duration?d:c},{duration:0}))&&0<b.startTime&&0<b.responseEnd&&(Z("wffs",Wt(b.startTime)),Z("wffe",Wt(b.responseEnd)))}
var Ou=window;Ou.ytcsi&&(Ou.ytcsi.info=Ju,Ou.ytcsi.tick=Z);var Pu="tokens consistency mss client_location entities response_received_commands store PLAYER_PRELOAD".split(" "),Qu=["type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseResponse"];function Ru(a,b,c,d){this.m=a;this.L=b;this.l=c;this.j=d;this.i=void 0;this.h=new Map;a.Pa||(a.Pa={});a.Pa=Object.assign({},Ht,a.Pa)}
function Su(a,b,c,d){if(void 0!==Ru.h){if(d=Ru.h,a=[a!==d.m,b!==d.L,c!==d.l,!1,!1,void 0!==d.i],a.some(function(e){return e}))throw new P("InnerTubeTransportService is already initialized",a);
}else Ru.h=new Ru(a,b,c,d)}
function Tu(a){var b={signalServiceEndpoint:{signal:"GET_DATASYNC_IDS"}};var c=void 0===c?pt:c;var d=zt(b,a.m);if(!d)return Gf(new P("Error: No request builder found for command.",b));var e=d.m(b,void 0,c);return e?new Bf(function(f){var g,h,l;return x(function(m){if(1==m.h){h="cors"===(null==(g=e.xa)?void 0:g.mode)?"cors":void 0;if(a.l.vd){var q=e.config,r;q=null==q?void 0:null==(r=q.ab)?void 0:r.sessionIndex;r=ot({sessionIndex:q});l=Object.assign({},Uu(h),r);return m.u(2)}return v(m,Vu(e.config,
h),3)}2!=m.h&&(l=m.i);f(Wu(a,e,l));m.h=0})}):Gf(new P("Error: Failed to build request for command.",b))}
function Xu(a,b,c){var d;if(b&&!(null==b?0:null==(d=b.Pr)?0:d.Sr)&&a.j){d=p(Pu);for(var e=d.next();!e.done;e=d.next())e=e.value,a.j[e]&&a.j[e].handleResponse(b,c)}}
function Wu(a,b,c){var d,e,f,g,h,l,m,q,r,w,t,A,E,F,O,N,R,ca,U,rb,Wa,oa,I,ma,ea,He,Ie,td;return x(function(ra){switch(ra.h){case 1:ra.u(2);break;case 3:if((d=ra.i)&&!d.isExpired())return ra.return(Promise.resolve(d.h()));case 2:if(null==(e=b)?0:null==(f=e.ha)?0:f.context)for(g=p([]),h=g.next();!h.done;h=g.next())l=h.value,l.Lr(b.ha.context);if(null==(m=a.i)||!m.Qr(b.input,b.ha)){ra.u(4);break}return v(ra,a.i.Gr(b.input,b.ha),5);case 5:return q=ra.i,M("kevlar_process_local_innertube_responses_killswitch")||
Xu(a,q,b),ra.return(q);case 4:return(t=null==(w=b.config)?void 0:w.oa)&&a.h.has(t)&&M("web_memoize_inflight_requests")?r=a.h.get(t):(A=JSON.stringify(b.ha),O=null!=(F=null==(E=b.xa)?void 0:E.headers)?F:{},b.xa=Object.assign({},b.xa,{headers:Object.assign({},O,c)}),N=Object.assign({},b.xa),"POST"===b.xa.method&&(N=Object.assign({},N,{body:A})),(null==(R=b.config)?0:R.hd)&&Z(b.config.hd),ca=function(){return a.L.fetch(b.input,N,b.config)},r=ca(),t&&a.h.set(t,r)),v(ra,r,6);
case 6:if((U=ra.i)&&"error"in U&&(null==(rb=U)?0:null==(Wa=rb.error)?0:Wa.details))for(oa=U.error.details,I=p(oa),ma=I.next();!ma.done;ma=I.next())ea=ma.value,(He=ea["@type"])&&-1<Qu.indexOf(He)&&(delete ea["@type"],U=ea);t&&a.h.has(t)&&a.h.delete(t);(null==(Ie=b.config)?0:Ie.jd)&&Z(b.config.jd);if(U||null==(td=a.i)||!td.yr(b.input,b.ha)){ra.u(7);break}return v(ra,a.i.Fr(b.input,b.ha),8);case 8:U=ra.i;case 7:return Xu(a,U,b),ra.return(U||void 0)}})}
function Vu(a,b){var c,d,e,f;return x(function(g){if(1==g.h){e=null==(c=a)?void 0:null==(d=c.ab)?void 0:d.sessionIndex;var h=ot({sessionIndex:e});if(!(h instanceof Bf)){var l=new Bf(eb);Cf(l,2,h);h=l}return v(g,h,2)}f=g.i;return g.return(Promise.resolve(Object.assign({},Uu(b),f)))})}
function Uu(a){var b={"Content-Type":"application/json"};L("EOM_VISITOR_DATA")?b["X-Goog-EOM-Visitor-Id"]=L("EOM_VISITOR_DATA"):L("VISITOR_DATA")&&(b["X-Goog-Visitor-Id"]=L("VISITOR_DATA"));b["X-Youtube-Bootstrap-Logged-In"]=L("LOGGED_IN",!1);"cors"!==a&&((a=L("INNERTUBE_CONTEXT_CLIENT_NAME"))&&(b["X-Youtube-Client-Name"]=a),(a=L("INNERTUBE_CONTEXT_CLIENT_VERSION"))&&(b["X-Youtube-Client-Version"]=a),(a=L("CHROME_CONNECTED_HEADER"))&&(b["X-Youtube-Chrome-Connected"]=a),(a=L("DOMAIN_ADMIN_STATE"))&&
(b["X-Youtube-Domain-Admin-State"]=a));return b}
;var Yu=new br("INNERTUBE_TRANSPORT_TOKEN");var Zu=["share/get_web_player_share_panel"],$u=["feedback"],av=["notification/modify_channel_preference"],bv=["browse/edit_playlist"],cv=["subscription/subscribe"],dv=["subscription/unsubscribe"];function ev(){}
u(ev,Et);ev.prototype.j=function(){return cv};
ev.prototype.h=function(a){return nr(a,Lk)||void 0};
ev.prototype.i=function(a,b,c){c=void 0===c?{}:c;b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params);c.botguardResponse&&(a.botguardResponse=c.botguardResponse);c.feature&&(a.clientFeature=c.feature)};
fa.Object.defineProperties(ev.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function fv(){}
u(fv,Et);fv.prototype.j=function(){return dv};
fv.prototype.h=function(a){return nr(a,Kk)||void 0};
fv.prototype.i=function(a,b){b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params)};
fa.Object.defineProperties(fv.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function gv(){}
u(gv,Et);gv.prototype.j=function(){return $u};
gv.prototype.h=function(a){return nr(a,rj)||void 0};
gv.prototype.i=function(a,b,c){a.feedbackTokens=[];b.feedbackToken&&a.feedbackTokens.push(b.feedbackToken);if(b=b.cpn||c.cpn)a.feedbackContext={cpn:b};a.isFeedbackTokenUnencrypted=!!c.is_feedback_token_unencrypted;a.shouldMerge=!1;c.extra_feedback_tokens&&(a.shouldMerge=!0,a.feedbackTokens=a.feedbackTokens.concat(c.extra_feedback_tokens))};
fa.Object.defineProperties(gv.prototype,{l:{configurable:!0,enumerable:!0,get:function(){return!0}}});function hv(){}
u(hv,Et);hv.prototype.j=function(){return av};
hv.prototype.h=function(a){return nr(a,Jk)||void 0};
hv.prototype.i=function(a,b){b.params&&(a.params=b.params);b.secondaryParams&&(a.secondaryParams=b.secondaryParams)};function iv(){}
u(iv,Et);iv.prototype.j=function(){return bv};
iv.prototype.h=function(a){return nr(a,Ik)||void 0};
iv.prototype.i=function(a,b){b.actions&&(a.actions=b.actions);b.params&&(a.params=b.params);b.playlistId&&(a.playlistId=b.playlistId)};function jv(){}
u(jv,Et);jv.prototype.j=function(){return Zu};
jv.prototype.h=function(a){return nr(a,Hk)};
jv.prototype.i=function(a,b,c){c=void 0===c?{}:c;b.serializedShareEntity&&(a.serializedSharedEntity=b.serializedShareEntity);c.includeListId&&(a.includeListId=!0)};var dr=new br("NETWORK_SLI_TOKEN");function kv(a){this.h=a}
kv.prototype.fetch=function(a,b){var c=this,d,e;return x(function(f){c.h&&(d=nc(oc(5,Ec(a,"key")))||"/UNKNOWN_PATH",c.h.start(d));e=new window.Request(a,b);return M("web_fetch_promise_cleanup_killswitch")?f.return(Promise.resolve(fetch(e).then(function(g){return c.handleResponse(g)}).catch(function(g){us(g)}))):f.return(fetch(e).then(function(g){return c.handleResponse(g)}).catch(function(g){us(g)}))})};
kv.prototype.handleResponse=function(a){var b=a.text().then(function(c){return JSON.parse(c.replace(")]}'",""))});
a.redirected||a.ok?this.h&&this.h.success():(this.h&&this.h.Cr(),b=b.then(function(c){us(new P("Error: API fetch failed",a.status,a.url,c));return Object.assign({},c,{errorMetadata:{status:a.status}})}));
return b};
kv[ar]=[new cr];var lv=new br("NETWORK_MANAGER_TOKEN");var mv;function nv(a){Ro.call(this,1,arguments);this.csn=a}
u(nv,Ro);var $o=new So("screen-created",nv),ov=[],qv=pv,rv=0;function sv(a,b,c,d,e,f,g){function h(){us(new P("newScreen() parent element does not have a VE - rootVe",b))}
var l=qv(),m=new Fs({veType:b,youtubeData:f,jspbYoutubeData:void 0});f={sequenceGroup:l};e&&(f.cttAuthInfo=e);M("il_via_jspb")?(e=Mj((new Lj).i(l),m.getAsJspb()),c&&c.visualElement?(m=new Nj,c.clientScreenNonce&&D(m,2,c.clientScreenNonce),Oj(m,c.visualElement.getAsJspb()),g&&D(m,4,hk[g]),G(e,Nj,5,m)):c&&h(),d&&D(e,3,d),ls(e,f,a)):(e={csn:l,pageVe:m.getAsJson()},c&&c.visualElement?(e.implicitGesture={parentCsn:c.clientScreenNonce,gesturedVe:c.visualElement.getAsJson()},g&&(e.implicitGesture.gestureType=
g)):c&&h(),d&&(e.cloneCsn=d),a?as("screenCreated",e,a,f):Em("screenCreated",e,f));Xo($o,new nv(l));return l}
function tv(a,b,c,d){var e=d.filter(function(l){l.csn!==b?(l.csn=b,l=!0):l=!1;return l}),f={cttAuthInfo:Os(b)||void 0,
sequenceGroup:b};d=p(d);for(var g=d.next();!g.done;g=d.next())g=g.value.getAsJson(),(sb(g)||!g.trackingParams&&!g.veType)&&us(Error("Child VE logged with no data"));if(M("il_via_jspb")){var h=Rj((new Pj).i(b),c.getAsJspb());jb(e,function(l){l=l.getAsJspb();de(h,3,Gj,l)});
"UNDEFINED_CSN"===b?uv("visualElementAttached",f,void 0,h):ms(h,f,a)}else c={csn:b,parentVe:c.getAsJson(),childVes:jb(e,function(l){return l.getAsJson()})},"UNDEFINED_CSN"===b?uv("visualElementAttached",f,c):a?as("visualElementAttached",c,a,f):Em("visualElementAttached",c,f)}
function vv(a,b,c,d,e,f){wv(a,b,c,e,f)}
function wv(a,b,c,d,e){var f={cttAuthInfo:Os(b)||void 0,sequenceGroup:b};M("il_via_jspb")?(d=(new Uj).i(b),c=c.getAsJspb(),c=G(d,Gj,2,c),c=D(c,4,1),e&&G(c,Jj,3,e),"UNDEFINED_CSN"===b?uv("visualElementShown",f,void 0,c):hs(c,f,a)):(e={csn:b,ve:c.getAsJson(),eventType:1},d&&(e.clientData=d),"UNDEFINED_CSN"===b?uv("visualElementShown",f,e):a?as("visualElementShown",e,a,f):Em("visualElementShown",e,f))}
function pv(){if(M("enable_web_96_bit_csn"))var a=Bs();else{a=Math.random()+"";for(var b=[],c=0,d=0;d<a.length;d++){var e=a.charCodeAt(d);255<e&&(b[c++]=e&255,e>>=8);b[c++]=e}a=cd(b,3)}return a}
function uv(a,b,c,d){ov.push({Fb:a,payload:c,ma:d,options:b});rv||(rv=ap())}
function bp(a){if(ov){for(var b=p(ov),c=b.next();!c.done;c=b.next())if(c=c.value,M("il_via_jspb")&&c.ma)switch(c.ma.i(a.csn),c.Fb){case "screenCreated":ls(c.ma,c.options);break;case "visualElementAttached":ms(c.ma,c.options);break;case "visualElementShown":hs(c.ma,c.options);break;case "visualElementHidden":is(c.ma,c.options);break;case "visualElementGestured":js(c.ma,c.options);break;case "visualElementStateChanged":ks(c.ma,c.options);break;default:us(new P("flushQueue unable to map payloadName to JSPB setter"))}else c.payload&&
(c.payload.csn=a.csn,Em(c.Fb,c.payload,c.options));ov.length=0}rv=0}
;function xv(){this.l=new Set;this.h=new Set;this.m=new Map;this.client=zq;this.csn=null}
function yv(){xv.h||(xv.h=new xv);return xv.h}
xv.prototype.i=function(a){this.client=a};
xv.prototype.j=function(){this.clear();this.csn=Ms()};
xv.prototype.clear=function(){this.l.clear();this.h.clear();this.m.clear();this.csn=null};function zv(){this.j=new Set;this.h=new Set;this.l=new Map;this.client=void 0;this.csn=null}
function Av(){zv.h||(zv.h=new zv);return zv.h}
zv.prototype.i=function(a){M("safe_logging_library_killswitch")?this.client=a:bl(yv().i).bind(yv())(a)};
zv.prototype.clear=function(){M("safe_logging_library_killswitch")?(this.j.clear(),this.h.clear(),this.l.clear(),this.csn=null):bl(yv().clear).bind(yv())()};function Bv(){this.j=new Set;this.h=new Set;this.l=new Map}
Bv.prototype.i=function(a){M("use_ts_visibilitylogger")&&Av().i(a)};
Bv.prototype.clear=function(){M("use_ts_visibilitylogger")?Av().clear():(this.j.clear(),this.h.clear(),this.l.clear())};
Pa(Bv);function Cv(){this.o=[];this.v=[];this.h=[];this.m=[];this.M=[];this.j=new Set;this.s=new Map}
Cv.prototype.i=function(a){this.client=a};
function Dv(a,b,c){c=void 0===c?0:c;b.then(function(d){a.j.has(c)&&a.l&&a.l();var e=Ms(c),f=Ks(c);if(e&&f){var g;(null==d?0:null==(g=d.response)?0:g.trackingParams)&&tv(a.client,e,f,[Gs(d.response.trackingParams)]);var h;(null==d?0:null==(h=d.playerResponse)?0:h.trackingParams)&&tv(a.client,e,f,[Gs(d.playerResponse.trackingParams)])}})}
function Ev(a,b,c,d){d=void 0===d?0:d;if(a.j.has(d))a.o.push([b,c]);else{var e=Ms(d);c=c||Ks(d);e&&c&&tv(a.client,e,c,[b])}}
Cv.prototype.clickCommand=function(a,b,c){var d=a.clickTrackingParams;c=void 0===c?0:c;if(d)if(c=Ms(void 0===c?0:c)){a=this.client;var e=Gs(d);d={cttAuthInfo:Os(c)||void 0,sequenceGroup:c};M("il_via_jspb")?(b=(new Sj).i(c),e=e.getAsJspb(),b=G(b,Gj,2,e),D(b,4,hk.INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK),"UNDEFINED_CSN"===c?uv("visualElementGestured",d,void 0,b):js(b,d,a)):(e={csn:c,ve:e.getAsJson(),gestureType:"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK"},b&&(e.clientData=b),"UNDEFINED_CSN"===
c?uv("visualElementGestured",d,e):a?as("visualElementGestured",e,a,d):Em("visualElementGestured",e,d));b=!0}else b=!1;else b=!1;return b};
Cv.prototype.visualElementStateChanged=function(a,b,c){c=void 0===c?0:c;0===c&&this.j.has(c)?this.v.push([a,b]):Fv(this,a,b,c)};
function Fv(a,b,c,d){d=void 0===d?0:d;var e=Ms(d);d=b||Ks(d);e&&d&&(a=a.client,b={cttAuthInfo:Os(e)||void 0,sequenceGroup:e},M("il_via_jspb")?(c=new Vj,c.i(e),d=d.getAsJspb(),G(c,Gj,2,d),"UNDEFINED_CSN"===e?uv("visualElementStateChanged",b,void 0,c):ks(c,b,a)):(c={csn:e,ve:d.getAsJson(),clientData:c},"UNDEFINED_CSN"===e?uv("visualElementStateChanged",b,c):a?as("visualElementStateChanged",c,a,b):Em("visualElementStateChanged",c,b)))}
function Gv(a,b,c){c=void 0===c?{}:c;a.j.add(c.layer||0);a.l=function(){Hv(a,b,c);var f=Ks(c.layer);if(f){for(var g=p(a.o),h=g.next();!h.done;h=g.next())h=h.value,Ev(a,h[0],h[1]||f,c.layer);f=p(a.v);for(g=f.next();!g.done;g=f.next())g=g.value,Fv(a,g[0],g[1])}};
Ms(c.layer)||a.l();if(c.Xb)for(var d=p(c.Xb),e=d.next();!e.done;e=d.next())Dv(a,e.value,c.layer);else ts(Error("Delayed screen needs a data promise."))}
function Hv(a,b,c){c=void 0===c?{}:c;c.layer||(c.layer=0);var d=void 0!==c.cd?c.cd:c.layer;var e=Ms(d);d=Ks(d);var f;d&&(void 0!==c.parentCsn?f={clientScreenNonce:c.parentCsn,visualElement:d}:e&&"UNDEFINED_CSN"!==e&&(f={clientScreenNonce:e,visualElement:d}));var g,h=L("EVENT_ID");"UNDEFINED_CSN"===e&&h&&(g={servletData:{serializedServletEventId:h}});try{var l=sv(a.client,b,f,c.Wb,c.cttAuthInfo,g,c.Dr)}catch(m){ws(m,{Nr:b,rootVe:d,Kr:void 0,zr:e,Jr:f,Wb:c.Wb});ts(m);return}Ps(l,b,c.layer,c.cttAuthInfo);
if(b=e&&"UNDEFINED_CSN"!==e&&d){a:{b=p(Object.values(Es));for(f=b.next();!f.done;f=b.next())if(Ms(f.value)===e){b=!0;break a}b=!1}b=!b}b&&(b=a.client,g=!0,h=(g=void 0===g?!1:g)?16:8,f={cttAuthInfo:Os(e)||void 0,sequenceGroup:e,endOfSequence:g},M("il_via_jspb")?(h=(new Tj).i(e),d=d.getAsJspb(),d=G(h,Gj,2,d),D(d,4,g?16:8),"UNDEFINED_CSN"===e?uv("visualElementHidden",f,void 0,d):is(d,f,b)):(d={csn:e,ve:d.getAsJson(),eventType:h},"UNDEFINED_CSN"===e?uv("visualElementHidden",f,d):b?as("visualElementHidden",
d,b,f):Em("visualElementHidden",d,f)));a.h[a.h.length-1]&&!a.h[a.h.length-1].csn&&(a.h[a.h.length-1].csn=l||"");Ku({clientScreenNonce:l});d=Bv.getInstance();M("use_ts_visibilitylogger")?(d=Av(),M("safe_logging_library_killswitch")?(d.clear(),d.csn=Ms()):bl(yv().j).bind(yv())()):d.clear();d=Ks(c.layer);e&&"UNDEFINED_CSN"!==e&&d&&(M("web_mark_root_visible")||M("music_web_mark_root_visible"))&&(e=l,M("safe_logging_library_killswitch")?wv(void 0,e,d):bl(vv)(void 0,e,d,void 0,void 0,void 0));a.j.delete(c.layer||
0);a.l=void 0;e=p(a.s);for(l=e.next();!l.done;l=e.next())b=p(l.value),l=b.next().value,b=b.next().value,b.has(c.layer)&&d&&Ev(a,l,d,c.layer);for(c=0;c<a.m.length;c++){e=a.m[c];try{e()}catch(m){ts(m)}}for(c=a.m.length=0;c<a.M.length;c++){e=a.M[c];try{e()}catch(m){ts(m)}}}
;function Iv(){var a,b,c;return x(function(d){if(1==d.h)return a=ir().resolve(Yu),a?v(d,Tu(a),2):(us(Error("InnertubeTransportService unavailable in fetchDatasyncIds")),d.return(void 0));if(b=d.i){if(b.errorMetadata)return us(Error("Datasync IDs fetch responded with "+b.errorMetadata.status+": "+b.error)),d.return(void 0);c=b.Ar;return d.return(c)}us(Error("Network request to get Datasync IDs failed."));return d.return(void 0)})}
;var Jv=y.caches,Kv;function Lv(a){var b=a.indexOf(":");return-1===b?{jc:a}:{jc:a.substring(0,b),datasyncId:a.substring(b+1)}}
function Mv(){return x(function(a){if(void 0!==Kv)return a.return(Kv);Kv=new Promise(function(b){var c;return x(function(d){switch(d.h){case 1:return za(d,2),v(d,Jv.open("test-only"),4);case 4:return v(d,Jv.delete("test-only"),5);case 5:Aa(d,3);break;case 2:if(c=Ba(d),c instanceof Error&&"SecurityError"===c.name)return b(!1),d.return();case 3:b("caches"in window),d.h=0}})});
return a.return(Kv)})}
function Nv(a){var b,c,d,e,f,g,h;x(function(l){if(1==l.h)return v(l,Mv(),2);if(3!=l.h){if(!l.i)return l.return(!1);b=[];return v(l,Jv.keys(),3)}c=l.i;d=p(c);for(e=d.next();!e.done;e=d.next())f=e.value,g=Lv(f),h=g.datasyncId,!h||a.includes(h)||b.push(Jv.delete(f));return l.return(Promise.all(b).then(function(m){return m.some(function(q){return q})}))})}
function Ov(){var a,b,c,d,e,f,g;return x(function(h){if(1==h.h)return v(h,Mv(),2);if(3!=h.h){if(!h.i)return h.return(!1);a=um("cache contains other");return v(h,Jv.keys(),3)}b=h.i;c=p(b);for(d=c.next();!d.done;d=c.next())if(e=d.value,f=Lv(e),(g=f.datasyncId)&&g!==a)return h.return(!0);return h.return(!1)})}
;function Pv(){try{return!!self.localStorage}catch(a){return!1}}
;function Qv(a){a=a.match(/(.*)::.*::.*/);if(null!==a)return a[1]}
function Rv(a){if(Pv()){var b=Object.keys(window.localStorage);b=p(b);for(var c=b.next();!c.done;c=b.next()){c=c.value;var d=Qv(c);void 0===d||a.includes(d)||self.localStorage.removeItem(c)}}}
function Sv(){if(!Pv())return!1;var a=um(),b=Object.keys(window.localStorage);b=p(b);for(var c=b.next();!c.done;c=b.next())if(c=Qv(c.value),void 0!==c&&c!==a)return!0;return!1}
;function Tv(){Iv().then(function(a){a&&(Tn(a),Nv(a),Rv(a))})}
function Uv(){var a=new nq;fi.S(function(){var b,c,d,e;return x(function(f){switch(f.h){case 1:if(M("ytidb_clear_optimizations_killswitch")){f.u(2);break}b=um("clear");if(b.startsWith("V")){var g=[b];Tn(g);Nv(g);Rv(g);return f.return()}c=Sv();return v(f,Ov(),3);case 3:return d=f.i,v(f,Un(),4);case 4:if(e=f.i,!c&&!d&&!e)return f.return();case 2:a.U()?Tv():a.l.add("publicytnetworkstatus-online",Tv,!0,void 0,void 0),f.h=0}})})}
;var Oh=ia(["data-"]);function Vv(a){a&&(a.dataset?a.dataset[Wv("loaded")]="true":Nh(a))}
function Xv(a,b){return a?a.dataset?a.dataset[Wv(b)]:a.getAttribute("data-"+b):null}
var Yv={};function Wv(a){return Yv[a]||(Yv[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Zv=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,$v=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/;function aw(a,b,c){c=void 0===c?null:c;if(window.spf&&spf.script){c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Zv,""),c=c.replace($v,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else bw(a,b,c)}
function bw(a,b,c){c=void 0===c?null:c;var d=cw(a),e=document.getElementById(d),f=e&&Xv(e,"loaded"),g=e&&!f;f?b&&b():(b&&(f=Vq(d,b),b=""+Ta(b),dw[b]=f),g||(e=ew(a,d,function(){Xv(e,"loaded")||(Vv(e),Yq(d),tl($a(Zq,d),0))},c)))}
function ew(a,b,c,d){d=void 0===d?null:d;var e=of("SCRIPT");e.id=b;e.onload=function(){c&&setTimeout(c,0)};
e.onreadystatechange=function(){switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);Ph(e,Mb(a));a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function fw(a){a=cw(a);var b=document.getElementById(a);b&&(Zq(a),b.parentNode.removeChild(b))}
function gw(a,b){a&&b&&(a=""+Ta(b),(a=dw[a])&&Xq(a))}
function cw(a){var b=document.createElement("a");gc(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+lc(a)}
var dw={};var hw=[],iw=!1;function jw(){if(!M("disable_biscotti_fetch_for_ad_blocker_detection")&&!M("disable_biscotti_fetch_entirely_for_all_web_clients")&&at()){var a=L("PLAYER_VARS",{});if("1"!=ub(a)&&!bt(a)){var b=function(){iw=!0;"google_ad_status"in window?Rk("DCLKSTAT",1):Rk("DCLKSTAT",2)};
try{aw("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}hw.push(fi.S(function(){if(!(iw||"google_ad_status"in window)){try{gw("//static.doubleclick.net/instream/ad_status.js",b)}catch(c){}iw=!0;Rk("DCLKSTAT",3)}},5E3))}}}
function kw(){var a=Number(L("DCLKSTAT",0));return isNaN(a)?0:a}
;function lw(a){var b=this;var c=void 0===c?0:c;var d=void 0===d?sm():d;this.l=c;this.j=d;this.i=new Fh;this.h=a;a={};c=p(this.h.entries());for(d=c.next();!d.done;a={Fa:a.Fa,Ra:a.Ra},d=c.next()){var e=p(d.value);d=e.next().value;e=e.next().value;a.Ra=d;a.Fa=e;d=function(f){return function(){f.Fa.Bb();b.h[f.Ra].mb=!0;b.h.every(function(g){return!0===g.mb})&&b.i.resolve()}}(a);
e=om(d,mw(this,a.Fa));this.h[a.Ra]=Object.assign({},a.Fa,{Bb:d,jobId:e})}}
function nw(a){var b=Array.from(a.h.keys()).sort(function(d,e){return mw(a,a.h[e])-mw(a,a.h[d])});
b=p(b);for(var c=b.next();!c.done;c=b.next())c=a.h[c.value],void 0===c.jobId||c.mb||(a.j.ea(c.jobId),om(c.Bb,10))}
lw.prototype.cancel=function(){for(var a=p(this.h),b=a.next();!b.done;b=a.next())b=b.value,void 0===b.jobId||b.mb||this.j.ea(b.jobId),b.mb=!0;this.i.resolve()};
function mw(a,b){var c;return null!=(c=b.priority)?c:a.l}
;function qw(a){this.state=a;this.plugins=[];this.o=void 0}
qw.prototype.install=function(){this.plugins.push.apply(this.plugins,ja(Ka.apply(0,arguments)))};
qw.prototype.uninstall=function(){var a=this;Ka.apply(0,arguments).forEach(function(b){b=a.plugins.indexOf(b);-1<b&&a.plugins.splice(b,1)})};
qw.prototype.transition=function(a,b){var c=this,d=this.v.find(function(f){return Array.isArray(f.from)?f.from.find(function(g){return g===c.state&&f.D===a}):f.from===c.state&&f.D===a});
if(d){this.j&&(nw(this.j),this.j=void 0);this.state=a;d=d.action.bind(this);var e=this.plugins.filter(function(f){return f[a]}).map(function(f){return f[a]});
d(rw(this,e,this.o),b)}else throw Error("no transition specified from "+this.state+" to "+a);};
function rw(a,b,c){return function(){var d=Ka.apply(0,arguments),e=b.filter(function(l){var m;return 10===(null!=(m=null!=c?c:l.priority)?m:0)}),f=b.filter(function(l){var m;
return 10!==(null!=(m=null!=c?c:l.priority)?m:0)});
sm();var g={};e=p(e);for(var h=e.next();!h.done;g={Sa:g.Sa},h=e.next())g.Sa=h.value,qm(function(l){return function(){l.Sa.callback.apply(l.Sa,ja(d))}}(g));
f=f.map(function(l){var m;return{Bb:function(){l.callback.apply(l,ja(d))},
priority:null!=(m=null!=c?c:l.priority)?m:0}});
f.length&&(a.j=new lw(f))}}
fa.Object.defineProperties(qw.prototype,{currentState:{configurable:!0,enumerable:!0,get:function(){return this.state}}});function sw(a){qw.call(this,void 0===a?"document_active":a);var b=this;this.o=10;this.h=new Map;this.v=[{from:"document_active",D:"document_disposed_preventable",action:this.M},{from:"document_active",D:"document_disposed",action:this.l},{from:"document_disposed_preventable",D:"document_disposed",action:this.l},{from:"document_disposed_preventable",D:"flush_logs",action:this.m},{from:"document_disposed_preventable",D:"document_active",action:this.i},{from:"document_disposed",D:"flush_logs",action:this.m},
{from:"document_disposed",D:"document_active",action:this.i},{from:"document_disposed",D:"document_disposed",action:function(){}},
{from:"flush_logs",D:"document_active",action:this.i}];window.addEventListener("pagehide",function(c){b.transition("document_disposed",{event:c})});
window.addEventListener("beforeunload",function(c){b.transition("document_disposed_preventable",{event:c})})}
u(sw,qw);sw.prototype.M=function(a,b){if(!this.h.get("document_disposed_preventable")){a(null==b?void 0:b.event);var c,d;if((null==b?0:null==(c=b.event)?0:c.defaultPrevented)||(null==b?0:null==(d=b.event)?0:d.returnValue)){b.event.returnValue||(b.event.returnValue=!0);b.event.defaultPrevented||b.event.preventDefault();this.h=new Map;this.transition("document_active");return}}this.h.set("document_disposed_preventable",!0);this.h.get("document_disposed")?this.transition("flush_logs"):this.transition("document_disposed")};
sw.prototype.l=function(a,b){this.h.get("document_disposed")?this.transition("document_active"):(a(null==b?void 0:b.event),this.h.set("document_disposed",!0),this.transition("flush_logs"))};
sw.prototype.m=function(a,b){a(null==b?void 0:b.event);this.transition("document_active")};
sw.prototype.i=function(){this.h=new Map};function tw(a){qw.call(this,void 0===a?"document_visibility_unknown":a);var b=this;this.v=[{from:"document_visibility_unknown",D:"document_visible",action:this.i},{from:"document_visibility_unknown",D:"document_hidden",action:this.h},{from:"document_visibility_unknown",D:"document_foregrounded",action:this.m},{from:"document_visibility_unknown",D:"document_backgrounded",action:this.l},{from:"document_visible",D:"document_hidden",action:this.h},{from:"document_visible",D:"document_foregrounded",action:this.m},
{from:"document_visible",D:"document_visible",action:this.i},{from:"document_foregrounded",D:"document_visible",action:this.i},{from:"document_foregrounded",D:"document_hidden",action:this.h},{from:"document_foregrounded",D:"document_foregrounded",action:this.m},{from:"document_hidden",D:"document_visible",action:this.i},{from:"document_hidden",D:"document_backgrounded",action:this.l},{from:"document_hidden",D:"document_hidden",action:this.h},{from:"document_backgrounded",D:"document_hidden",action:this.h},
{from:"document_backgrounded",D:"document_backgrounded",action:this.l},{from:"document_backgrounded",D:"document_visible",action:this.i}];document.addEventListener("visibilitychange",function(c){"visible"===document.visibilityState?b.transition("document_visible",{event:c}):b.transition("document_hidden",{event:c})});
M("visibility_lifecycles_dynamic_backgrounding")&&(window.addEventListener("blur",function(c){b.transition("document_backgrounded",{event:c})}),window.addEventListener("focus",function(c){b.transition("document_foregrounded",{event:c})}))}
u(tw,qw);tw.prototype.i=function(a,b){a(null==b?void 0:b.event);M("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_foregrounded")};
tw.prototype.h=function(a,b){a(null==b?void 0:b.event);M("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_backgrounded")};
tw.prototype.l=function(a,b){a(null==b?void 0:b.event)};
tw.prototype.m=function(a,b){a(null==b?void 0:b.event)};function uw(){this.h=new sw;this.i=new tw}
uw.prototype.install=function(){var a=Ka.apply(0,arguments);this.h.install.apply(this.h,ja(a));this.i.install.apply(this.i,ja(a))};function vw(){uw.call(this);var a={};this.install((a.document_disposed={callback:this.j},a));a={};this.install((a.flush_logs={callback:this.l},a))}
var ww;u(vw,uw);vw.prototype.l=function(){if(M("web_fp_via_jspb")){var a=new Fj,b=Ms();b&&D(a,1,b);b=new fk;be(b,Fj,380,gk,a);gs(b);M("web_fp_via_jspb_and_json")&&Em("finalPayload",{csn:Ms()})}else Em("finalPayload",{csn:Ms()})};
vw.prototype.j=function(){ys(zs)};function xw(){}
xw.getInstance=function(){var a=B("ytglobal.storage_");a||(a=new xw,z("ytglobal.storage_",a));return a};
xw.prototype.estimate=function(){var a,b,c;return x(function(d){a=navigator;return(null==(b=a.storage)?0:b.estimate)?d.return(a.storage.estimate()):(null==(c=a.webkitTemporaryStorage)?0:c.queryUsageAndQuota)?d.return(yw()):d.return()})};
function yw(){var a=navigator;return new Promise(function(b,c){var d;null!=(d=a.webkitTemporaryStorage)&&d.queryUsageAndQuota?a.webkitTemporaryStorage.queryUsageAndQuota(function(e,f){b({usage:e,quota:f})},function(e){c(e)}):c(Error("webkitTemporaryStorage is not supported."))})}
z("ytglobal.storageClass_",xw);function Cm(a,b){var c=this;this.handleError=a;this.h=b;this.i=!1;void 0===self.document||self.addEventListener("beforeunload",function(){c.i=!0});
this.j=Math.random()<=Uk("ytidb_transaction_ended_event_rate_limit_session",.2)}
Cm.prototype.logEvent=function(a,b){switch(a){case "IDB_DATA_CORRUPTED":M("idb_data_corrupted_killswitch")||this.h("idbDataCorrupted",b);break;case "IDB_UNEXPECTEDLY_CLOSED":this.h("idbUnexpectedlyClosed",b);break;case "IS_SUPPORTED_COMPLETED":M("idb_is_supported_completed_killswitch")||this.h("idbIsSupportedCompleted",b);break;case "QUOTA_EXCEEDED":zw(this,b);break;case "TRANSACTION_ENDED":this.j&&Math.random()<=Uk("ytidb_transaction_ended_event_rate_limit_transaction",.1)&&this.h("idbTransactionEnded",
b);break;case "TRANSACTION_UNEXPECTEDLY_ABORTED":a=Object.assign({},b,{hasWindowUnloaded:this.i}),this.h("idbTransactionAborted",a)}};
function zw(a,b){xw.getInstance().estimate().then(function(c){c=Object.assign({},b,{isSw:void 0===self.document,isIframe:self!==self.top,deviceStorageUsageMbytes:Aw(null==c?void 0:c.usage),deviceStorageQuotaMbytes:Aw(null==c?void 0:c.quota)});a.h("idbQuotaExceeded",c)})}
function Aw(a){return"undefined"===typeof a?"-1":String(Math.ceil(a/1048576))}
;function Bw(a,b,c){J.call(this);var d=this;c=c||L("POST_MESSAGE_ORIGIN")||window.document.location.protocol+"//"+window.document.location.hostname;this.l=b||null;this.targetOrigin="*";this.m=c;this.sessionId=null;this.i="widget";this.I=!!a;this.F=function(e){a:if(!("*"!=d.m&&e.origin!=d.m||d.l&&e.source!=d.l||"string"!==typeof e.data)){try{var f=JSON.parse(e.data)}catch(g){break a}if(!(null==f||d.I&&(d.sessionId&&d.sessionId!=f.id||d.i&&d.i!=f.channel))&&f)switch(f.event){case "listening":"null"!=
e.origin&&(d.m=d.targetOrigin=e.origin);d.l=e.source;d.sessionId=f.id;d.j&&(d.j(),d.j=null);break;case "command":d.o&&(!d.s||0<=gb(d.s,f.func))&&d.o(f.func,f.args,e.origin)}}};
this.s=this.j=this.o=null;window.addEventListener("message",this.F)}
u(Bw,J);Bw.prototype.sendMessage=function(a,b){if(b=b||this.l){this.sessionId&&(a.id=this.sessionId);this.i&&(a.channel=this.i);try{var c=JSON.stringify(a);b.postMessage(c,this.targetOrigin)}catch(d){dl(d)}}};
Bw.prototype.B=function(){window.removeEventListener("message",this.F);J.prototype.B.call(this)};function Cw(){this.i=[];this.isReady=!1;this.j={};var a=this.h=new Bw(!!L("WIDGET_ID_ENFORCE")),b=this.ed.bind(this);a.o=b;a.s=null;this.h.i="widget";if(a=L("WIDGET_ID"))this.h.sessionId=a}
k=Cw.prototype;k.ed=function(a,b,c){"addEventListener"===a&&b?this.Ab(b[0],c):this.Lb(a,b,c)};
k.Lb=function(){};
k.tb=function(a){var b=this;return function(c){return b.sendMessage(a,c)}};
k.Ab=function(a,b){this.j[a]||"onReady"===a||(this.addEventListener(a,this.tb(a,b)),this.j[a]=!0)};
k.addEventListener=function(){};
k.Pc=function(){this.isReady=!0;this.sendMessage("initialDelivery",this.wb());this.sendMessage("onReady");hb(this.i,this.pc,this);this.i=[]};
k.wb=function(){return null};
function Dw(a,b){a.sendMessage("infoDelivery",b)}
k.pc=function(a){this.isReady?this.h.sendMessage(a):this.i.push(a)};
k.sendMessage=function(a,b){this.pc({event:a,info:void 0===b?null:b})};
k.dispose=function(){this.h=null};var Ew={},Fw=(Ew["api.invalidparam"]=2,Ew.auth=150,Ew["drm.auth"]=150,Ew["heartbeat.net"]=150,Ew["heartbeat.servererror"]=150,Ew["heartbeat.stop"]=150,Ew["html5.unsupportedads"]=5,Ew["fmt.noneavailable"]=5,Ew["fmt.decode"]=5,Ew["fmt.unplayable"]=5,Ew["html5.missingapi"]=5,Ew["html5.unsupportedlive"]=5,Ew["drm.unavailable"]=5,Ew["mrm.blocked"]=151,Ew);var Gw=new Set("endSeconds startSeconds mediaContentUrl suggestedQuality videoId rct rctn".split(" "));function Hw(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function Iw(a,b,c){if("string"===typeof a)return{videoId:a,startSeconds:b,suggestedQuality:c};b={};c=p(Gw);for(var d=c.next();!d.done;d=c.next())d=d.value,a[d]&&(b[d]=a[d]);return b}
function Jw(a,b,c,d){if(Sa(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};"string"===typeof a&&16===a.length?b.list="PL"+a:b.playlist=a;return b}
;function Kw(a){Cw.call(this);this.listeners=[];this.l=!1;this.api=a;this.addEventListener("onReady",this.onReady.bind(this));this.addEventListener("onVideoProgress",this.pd.bind(this));this.addEventListener("onVolumeChange",this.qd.bind(this));this.addEventListener("onApiChange",this.kd.bind(this));this.addEventListener("onPlaybackQualityChange",this.md.bind(this));this.addEventListener("onPlaybackRateChange",this.nd.bind(this));this.addEventListener("onStateChange",this.od.bind(this));this.addEventListener("onWebglSettingsChanged",
this.rd.bind(this))}
u(Kw,Cw);k=Kw.prototype;
k.Lb=function(a,b,c){if(this.api.isExternalMethodAvailable(a,c)){b=b||[];if(0<b.length&&Hw(a)){var d=b;if(Sa(d[0])&&!Array.isArray(d[0]))var e=d[0];else switch(e={},a){case "loadVideoById":case "cueVideoById":e=Iw(d[0],void 0!==d[1]?Number(d[1]):void 0,d[2]);break;case "loadVideoByUrl":case "cueVideoByUrl":e=d[0];"string"===typeof e&&(e={mediaContentUrl:e,startSeconds:void 0!==d[1]?Number(d[1]):void 0,suggestedQuality:d[2]});b:{if((d=e.mediaContentUrl)&&(d=/\/([ve]|embed)\/([^#?]+)/.exec(d))&&d[2]){d=
d[2];break b}d=null}e.videoId=d;e=Iw(e);break;case "loadPlaylist":case "cuePlaylist":e=Jw(d[0],d[1],d[2],d[3])}b.length=1;b[0]=e}this.api.handleExternalCall(a,b,c);Hw(a)&&Dw(this,this.wb())}};
k.Ab=function(a,b){("onReady"===a||"onError"===a&&this.l)&&this.api.logApiCall(a+" invocation",b);this.api.logApiCall(a+" registration",b);Cw.prototype.Ab.call(this,a,b)};
k.tb=function(a,b){var c=this,d=Cw.prototype.tb.call(this,a,b);return function(e){c.api.logApiCall(a+" invocation",b);d(e)}};
k.onReady=function(){var a=this.Pc.bind(this);this.h.j=a;a=this.api.getVideoData();if(!a.isPlayable){this.l=!0;a=a.errorCode;var b=void 0===b?5:b;this.sendMessage("onError",(a?Fw[a]||b:b).toString())}};
k.addEventListener=function(a,b){this.listeners.push({eventType:a,listener:b});this.api.addEventListener(a,b)};
k.wb=function(){if(!this.api)return null;var a=this.api.getApiInterface();mb(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c];if(0===e.search("get")||0===e.search("is")){var f=0;0===e.search("get")?f=3:0===e.search("is")&&(f=2);f=e.charAt(f).toLowerCase()+e.substr(f+1);try{var g=this.api[e]();b[f]=g}catch(h){}}}b.videoData=this.api.getVideoData();b.currentTimeLastUpdated_=Date.now()/1E3;return b};
k.od=function(a){a={playerState:a,currentTime:this.api.getCurrentTime(),duration:this.api.getDuration(),videoData:this.api.getVideoData(),videoStartBytes:0,videoBytesTotal:this.api.getVideoBytesTotal(),videoLoadedFraction:this.api.getVideoLoadedFraction(),playbackQuality:this.api.getPlaybackQuality(),availableQualityLevels:this.api.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getVideoUrl&&
(a.videoUrl=this.api.getVideoUrl());this.api.getVideoContentRect&&(a.videoContentRect=this.api.getVideoContentRect());this.api.getProgressState&&(a.progressState=this.api.getProgressState());this.api.getPlaylist&&(a.playlist=this.api.getPlaylist());this.api.getPlaylistIndex&&(a.playlistIndex=this.api.getPlaylistIndex());this.api.getStoryboardFormat&&(a.storyboardFormat=this.api.getStoryboardFormat());Dw(this,a)};
k.md=function(a){Dw(this,{playbackQuality:a})};
k.nd=function(a){Dw(this,{playbackRate:a})};
k.kd=function(){for(var a=this.api.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.api.getOptions(e);b[e]={options:f};for(var g=0,h=f.length;g<h;g++){var l=f[g],m=this.api.getOption(e,l);b[e][l]=m}}this.sendMessage("apiInfoDelivery",b)};
k.qd=function(){Dw(this,{muted:this.api.isMuted(),volume:this.api.getVolume()})};
k.pd=function(a){a={currentTime:a,videoBytesLoaded:this.api.getVideoBytesLoaded(),videoLoadedFraction:this.api.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getProgressState&&(a.progressState=this.api.getProgressState());Dw(this,a)};
k.rd=function(){var a={sphericalProperties:this.api.getSphericalProperties()};Dw(this,a)};
k.dispose=function(){Cw.prototype.dispose.call(this);for(var a=0;a<this.listeners.length;a++){var b=this.listeners[a];this.api.removeEventListener(b.eventType,b.listener)}this.listeners=[]};function Lw(a){J.call(this);this.i={};this.started=!1;this.connection=a;this.connection.subscribe("command",this.lc,this)}
u(Lw,J);k=Lw.prototype;k.start=function(){this.started||this.h()||(this.started=!0,this.connection.ya("RECEIVING"))};
k.ya=function(a,b){this.started&&!this.h()&&this.connection.ya(a,b)};
k.lc=function(a,b,c){if(this.started&&!this.h()){var d=b||{};switch(a){case "addEventListener":"string"===typeof d.event&&this.addListener(d.event);break;case "removeEventListener":"string"===typeof d.event&&this.removeListener(d.event);break;default:this.api.isReady()&&this.api.isExternalMethodAvailable(a,c||null)&&(b=Mw(a,b||{}),c=this.api.handleExternalCall(a,b,c||null),(c=Nw(a,c))&&this.ya(a,c))}}};
k.addListener=function(a){if(!(a in this.i)){var b=this.ld.bind(this,a);this.i[a]=b;this.addEventListener(a,b)}};
k.ld=function(a,b){this.started&&!this.h()&&this.connection.ya(a,this.vb(a,b))};
k.vb=function(a,b){if(null!=b)return{value:b}};
k.removeListener=function(a){a in this.i&&(this.removeEventListener(a,this.i[a]),delete this.i[a])};
k.B=function(){var a=this.connection;a.h()||Ci(a.i,"command",this.lc,this);this.connection=null;for(var b in this.i)this.i.hasOwnProperty(b)&&this.removeListener(b);J.prototype.B.call(this)};function Ow(a,b){Lw.call(this,b);this.api=a;this.start()}
u(Ow,Lw);Ow.prototype.addEventListener=function(a,b){this.api.addEventListener(a,b)};
Ow.prototype.removeEventListener=function(a,b){this.api.removeEventListener(a,b)};
function Mw(a,b){switch(a){case "loadVideoById":return a=Iw(b),[a];case "cueVideoById":return a=Iw(b),[a];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return a=Jw(b),[a];case "cuePlaylist":return a=Jw(b),[a];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];
case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function Nw(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
Ow.prototype.vb=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return Lw.prototype.vb.call(this,a,b)};
Ow.prototype.B=function(){Lw.prototype.B.call(this);delete this.api};function Pw(a){a=void 0===a?!1:a;J.call(this);this.i=new K(a);ve(this,this.i)}
ab(Pw,J);Pw.prototype.subscribe=function(a,b,c){return this.h()?0:this.i.subscribe(a,b,c)};
Pw.prototype.m=function(a,b){this.h()||this.i.sa.apply(this.i,arguments)};function Qw(a,b,c){Pw.call(this);this.l=a;this.j=b;this.id=c}
u(Qw,Pw);Qw.prototype.ya=function(a,b){this.h()||this.l.ya(this.j,this.id,a,b)};
Qw.prototype.B=function(){this.j=this.l=null;Pw.prototype.B.call(this)};function Rw(a,b,c){J.call(this);this.i=a;this.origin=c;this.j=Iq(window,"message",this.l.bind(this));this.connection=new Qw(this,a,b);ve(this,this.connection)}
u(Rw,J);Rw.prototype.ya=function(a,b,c,d){this.h()||a!==this.i||(a={id:b,command:c},d&&(a.data=d),this.i.postMessage(JSON.stringify(a),this.origin))};
Rw.prototype.l=function(a){if(!this.h()&&a.origin===this.origin){var b=a.data;if("string"===typeof b){try{b=JSON.parse(b)}catch(d){return}if(b.command){var c=this.connection;c.h()||c.m("command",b.command,b.data,a.origin)}}}};
Rw.prototype.B=function(){Jq(this.j);this.i=null;J.prototype.B.call(this)};function Sw(){this.state=1;this.h=null}
k=Sw.prototype;
k.initialize=function(a,b,c){if(a.program){var d,e=null!=(d=a.interpreterScript)?d:null,f;d=null!=(f=a.interpreterUrl)?f:null;a.interpreterSafeScript&&(e=a.interpreterSafeScript,Eb("From proto message. b/166824318"),e=e.privateDoNotAccessOrElseSafeScriptWrappedValue||"",e=(f=Bb())?f.createScript(e):e,e=(new Gb(e)).toString());a.interpreterSafeUrl&&(d=a.interpreterSafeUrl,Eb("From proto message. b/166824318"),d=Mb(d.privateDoNotAccessOrElseTrustedResourceUrlWrappedValue||"").toString());Tw(this,e,
d,a.program,b,c)}else us(Error("Cannot initialize botguard without program"))};
function Tw(a,b,c,d,e,f){var g=void 0===g?"trayride":g;c?(a.state=2,aw(c,function(){window[g]?Uw(a,d,g,e):(a.state=3,fw(c),us(new P("Unable to load Botguard","from "+c)))},f)):b?(f=of("SCRIPT"),f.textContent=b,f.nonce=jc(),document.head.appendChild(f),document.head.removeChild(f),window[g]?Uw(a,d,g,e):(a.state=4,us(new P("Unable to load Botguard from JS")))):us(new P("Unable to load VM; no url or JS provided"))}
function Uw(a,b,c,d){a.state=5;try{var e=new Gh({program:b,Sc:c,fd:M("att_web_record_metrics")});e.sd.then(function(){a.state=6;d&&d(b)});
a.Jb(e)}catch(f){a.state=7,f instanceof Error&&us(f)}}
k.invoke=function(a){a=void 0===a?{}:a;return this.Kb()?this.xc({Vb:a}):null};
k.dispose=function(){this.Mb()};
k.Mb=function(){this.Jb(null);this.state=8};
k.Kb=function(){return!!this.h};
k.xc=function(a){return this.h.sc(a)};
k.Jb=function(a){te(this.h);this.h=a};function Vw(){var a=B("yt.abuse.playerAttLoader");return a&&["bgvma","bgvmb","bgvmc"].every(function(b){return b in a})?a:null}
;function Ww(){Sw.apply(this,arguments)}
u(Ww,Sw);Ww.prototype.Mb=function(){this.state=8};
Ww.prototype.Jb=function(a){var b;null==(b=Vw())||b.bgvma();a?(b={bgvma:a.dispose.bind(a),bgvmb:a.snapshot.bind(a),bgvmc:a.sc.bind(a)},z("yt.abuse.playerAttLoader",b),z("yt.abuse.playerAttLoaderRun",function(c){return a.snapshot(c)})):(z("yt.abuse.playerAttLoader",null),z("yt.abuse.playerAttLoaderRun",null))};
Ww.prototype.Kb=function(){return!!Vw()};
Ww.prototype.xc=function(a){return Vw().bgvmc(a)};var Xw=new Ww;function Yw(){return Xw.Kb()}
function Zw(a){a=void 0===a?{}:a;return Xw.invoke(a)}
;function $w(a){a=a||{};var b={},c={};this.url=a.url||"";this.args=a.args||wb(b);this.assets=a.assets||{};this.attrs=a.attrs||wb(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
$w.prototype.clone=function(){var a=new $w,b;for(b in this)if(this.hasOwnProperty(b)){var c=this[b];"object"==Qa(c)?a[b]=wb(c):a[b]=c}return a};var ax=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;function bx(a){a=a||"";if(window.spf){var b=a.match(ax);spf.style.load(a,b?b[1]:"",void 0)}else cx(a)}
function cx(a){var b=dx(a),c=document.getElementById(b),d=c&&Xv(c,"loaded");d||c&&!d||(c=ex(a,b,function(){Xv(c,"loaded")||(Vv(c),Yq(b),tl($a(Zq,b),0))}))}
function ex(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Mb(a);hc(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function dx(a){var b=of("A");Eb("This URL is never added to the DOM");gc(b,new Pb(a,Qb));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+lc(a)}
;function fx(){J.call(this);this.i=[]}
u(fx,J);fx.prototype.B=function(){for(;this.i.length;){var a=this.i.pop();a.target.removeEventListener(a.name,a.callback,void 0)}J.prototype.B.call(this)};function gx(){fx.apply(this,arguments)}
u(gx,fx);function hx(a,b,c,d,e){J.call(this);var f=this;this.s=b;this.webPlayerContextConfig=d;this.Xa=e;this.ca=!1;this.api={};this.V=this.o=null;this.K=new K;this.i={};this.P=this.W=this.elementId=this.ta=this.config=null;this.O=!1;this.l=this.F=null;this.ka={};this.Ya=["onReady"];this.lastError=null;this.Ha=NaN;this.I={};this.Za=new gx(this);this.T=0;this.j=this.m=a;ve(this,this.K);ix(this);jx(this);ve(this,this.Za);c?this.T=tl(function(){f.loadNewVideoConfig(c)},0):d&&(kx(this),lx(this))}
u(hx,J);k=hx.prototype;k.getId=function(){return this.s};
k.loadNewVideoConfig=function(a){if(!this.h()){this.T&&(window.clearTimeout(this.T),this.T=0);var b=a||{};b instanceof $w||(b=new $w(b));this.config=b;this.setConfig(a);lx(this);this.isReady()&&mx(this)}};
function kx(a){var b;a.webPlayerContextConfig?b=a.webPlayerContextConfig.rootElementId:b=a.config.attrs.id;a.elementId=b||a.elementId;"video-player"===a.elementId&&(a.elementId=a.s,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.s:a.config.attrs.id=a.s);var c;(null==(c=a.j)?void 0:c.id)===a.elementId&&(a.elementId+="-player",a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
k.setConfig=function(a){this.ta=a;this.config=nx(a);kx(this);if(!this.W){var b;this.W=ox(this,(null==(b=this.config.args)?void 0:b.jsapicallback)||"onYouTubePlayerReady")}this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};var c;if(null==(c=this.config)?0:c.attrs)a=this.config.attrs,(b=a.width)&&this.j&&(this.j.style.width=Zh(Number(b)||b)),(a=a.height)&&this.j&&(this.j.style.height=Zh(Number(a)||a))};
function mx(a){if(a.config&&!0!==a.config.loaded)if(a.config.loaded=!0,!a.config.args||"0"!==a.config.args.autoplay&&0!==a.config.args.autoplay&&!1!==a.config.args.autoplay){var b;a.api.loadVideoByPlayerVars(null!=(b=a.config.args)?b:null)}else a.api.cueVideoByPlayerVars(a.config.args)}
function px(a){var b=!0,c=qx(a);c&&a.config&&(a=rx(a),b=Xv(c,"version")===a);return b&&!!B("yt.player.Application.create")}
function lx(a){if(!a.h()&&!a.O){var b=px(a);if(b&&"html5"===(qx(a)?"html5":null))a.P="html5",a.isReady()||sx(a);else if(tx(a),a.P="html5",b&&a.l&&a.m)a.m.appendChild(a.l),sx(a);else{a.config&&(a.config.loaded=!0);var c=!1;a.F=function(){c=!0;var d=ux(a,"player_bootstrap_method")?B("yt.player.Application.createAlternate")||B("yt.player.Application.create"):B("yt.player.Application.create");var e=a.config?nx(a.config):void 0;d&&d(a.m,e,a.webPlayerContextConfig,a.Xa);sx(a)};
a.O=!0;b?a.F():(aw(rx(a),a.F),(b=vx(a))&&bx(b),wx(a)&&!c&&z("yt.player.Application.create",null))}}}
function qx(a){var b=nf(a.elementId);!b&&a.j&&a.j.querySelector&&(b=a.j.querySelector("#"+a.elementId));return b}
function sx(a){if(!a.h()){var b=qx(a),c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);if(c){a.O=!1;if(!ux(a,"html5_remove_not_servable_check_killswitch")){var d;if((null==b?0:b.isNotServable)&&a.config&&(null==b?0:b.isNotServable(null==(d=a.config.args)?void 0:d.video_id)))return}xx(a)}else a.Ha=tl(function(){sx(a)},50)}}
function xx(a){ix(a);a.ca=!0;var b=qx(a);if(b){a.o=yx(a,b,"addEventListener");a.V=yx(a,b,"removeEventListener");var c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());for(var d=a.api,e=0;e<c.length;e++){var f=c[e];d[f]||(d[f]=yx(a,b,f))}}for(var g in a.i)a.i.hasOwnProperty(g)&&a.o&&a.o(g,a.i[g]);mx(a);a.W&&a.W(a.api);a.K.sa("onReady",a.api)}
function yx(a,b,c){var d=b[c];return function(){var e=Ka.apply(0,arguments);try{return a.lastError=null,d.apply(b,e)}catch(f){"sendAbandonmentPing"!==c&&(f.params=c,a.lastError=f,us(f))}}}
function ix(a){a.ca=!1;if(a.V)for(var b in a.i)a.i.hasOwnProperty(b)&&a.V(b,a.i[b]);for(var c in a.I)a.I.hasOwnProperty(c)&&window.clearTimeout(Number(c));a.I={};a.o=null;a.V=null;b=a.api;for(var d in b)b.hasOwnProperty(d)&&(b[d]=null);b.addEventListener=function(e,f){a.addEventListener(e,f)};
b.removeEventListener=function(e,f){a.removeEventListener(e,f)};
b.destroy=function(){a.dispose()};
b.getLastError=function(){return a.getLastError()};
b.getPlayerType=function(){return a.getPlayerType()};
b.getCurrentVideoConfig=function(){return a.ta};
b.loadNewVideoConfig=function(e){a.loadNewVideoConfig(e)};
b.isReady=function(){return a.isReady()}}
k.isReady=function(){return this.ca};
function jx(a){a.addEventListener("WATCH_LATER_VIDEO_ADDED",function(b){Yq("WATCH_LATER_VIDEO_ADDED",b)});
a.addEventListener("WATCH_LATER_VIDEO_REMOVED",function(b){Yq("WATCH_LATER_VIDEO_REMOVED",b)})}
k.addEventListener=function(a,b){var c=this,d=ox(this,b);d&&(0<=gb(this.Ya,a)||this.i[a]||(b=zx(this,a),this.o&&this.o(a,b)),this.K.subscribe(a,d),"onReady"===a&&this.isReady()&&tl(function(){d(c.api)},0))};
k.removeEventListener=function(a,b){this.h()||(b=ox(this,b))&&Ci(this.K,a,b)};
function ox(a,b){var c=b;if("string"===typeof b){if(a.ka[b])return a.ka[b];c=function(){var d=Ka.apply(0,arguments),e=B(b);if(e)try{e.apply(y,d)}catch(f){ts(f)}};
a.ka[b]=c}return c?c:null}
function zx(a,b){var c="ytPlayer"+b+a.s;a.i[b]=c;y[c]=function(d){var e=tl(function(){if(!a.h()){try{a.K.sa(b,null!=d?d:void 0)}catch(h){us(new P("PlayerProxy error when creating global callback",{error:h,event:b,playerId:a.s,data:d}))}var f=a.I,g=String(e);g in f&&delete f[g]}},0);
tb(a.I,String(e))};
return c}
k.getPlayerType=function(){return this.P||(qx(this)?"html5":null)};
k.getLastError=function(){return this.lastError};
function tx(a){a.cancel();ix(a);a.P=null;a.config&&(a.config.loaded=!1);var b=qx(a);b&&(px(a)||!wx(a)?a.l=b:(b&&b.destroy&&b.destroy(),a.l=null));if(a.m)for(a=a.m;b=a.firstChild;)a.removeChild(b)}
k.cancel=function(){this.F&&gw(rx(this),this.F);window.clearTimeout(this.Ha);this.O=!1};
k.B=function(){tx(this);if(this.l&&this.config&&this.l.destroy)try{this.l.destroy()}catch(b){ts(b)}this.ka=null;for(var a in this.i)this.i.hasOwnProperty(a)&&(y[this.i[a]]=null);this.ta=this.config=this.api=null;delete this.m;delete this.j;J.prototype.B.call(this)};
function wx(a){var b,c;a=null==(b=a.config)?void 0:null==(c=b.args)?void 0:c.fflags;return!!a&&-1!==a.indexOf("player_destroy_old_version=true")}
function rx(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function vx(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function ux(a,b){if(a.webPlayerContextConfig)var c=a.webPlayerContextConfig.serializedExperimentFlags;else{var d;if(null==(d=a.config)?0:d.args)c=a.config.args.fflags}return"true"===gl(c||"","&")[b]}
function nx(a){for(var b={},c=p(Object.keys(a)),d=c.next();!d.done;d=c.next()){d=d.value;var e=a[d];b[d]="object"===typeof e?wb(e):e}return b}
;var Ax={},Bx="player_uid_"+(1E9*Math.random()>>>0);function Cx(a,b){var c="player",d=!1;d=void 0===d?!0:d;c="string"===typeof c?nf(c):c;var e=Bx+"_"+Ta(c),f=Ax[e];if(f&&d)return Dx(a,b)?f.api.loadVideoByPlayerVars(a.args||null):f.loadNewVideoConfig(a),f.api;f=new hx(c,e,a,b,void 0);Ax[e]=f;Yq("player-added",f.api);we(f,function(){delete Ax[f.getId()]});
return f.api}
function Dx(a,b){return b&&b.serializedExperimentFlags?b.serializedExperimentFlags.includes("web_player_remove_playerproxy=true"):a&&a.args&&a.args.fflags?a.args.fflags.includes("web_player_remove_playerproxy=true"):!1}
;var Ex=null,Fx=null,Gx=null;function Hx(){Ix()}
function Jx(){Ix()}
function Ix(){var a=Ex.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
function Kx(){Ex&&Ex.sendAbandonmentPing&&Ex.sendAbandonmentPing();L("PL_ATT")&&Xw.dispose();for(var a=fi,b=0,c=hw.length;b<c;b++)a.ea(hw[b]);hw.length=0;fw("//static.doubleclick.net/instream/ad_status.js");iw=!1;Rk("DCLKSTAT",0);ue(Gx,Fx);Ex&&(Ex.removeEventListener("onVideoDataChange",Hx),Ex.destroy())}
;function Lx(a,b,c){a="ST-"+lc(a).toString(36);b=b?uc(b):"";c=c||5;at()&&Xl(a,b,c)}
;function Mx(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=L("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){d=a;var e=void 0===e?!0:e;var f=L("VALID_SESSION_TEMPDATA_DOMAINS",[]),g=pc(window.location.href);g&&f.push(g);g=pc(d);if(0<=gb(f,g)||!g&&0==d.lastIndexOf("/",0))if(M("autoescape_tempdata_url")&&(f=document.createElement("a"),gc(f,d),d=f.href),d&&(d=qc(d),f=d.indexOf("#"),d=0>f?d:d.slice(0,f)))if(e&&!b.csn&&(b.itct||b.ved)&&(b=Object.assign({csn:Ms()},b)),h){var h=parseInt(h,10);isFinite(h)&&0<h&&
Lx(d,b,h)}else Lx(d,b)}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var l=void 0===l?{}:l;var m=void 0===m?"":m;var q=void 0===q?window:q;c=q.location;a=wc(a,l)+m;var r=void 0===r?Sh:r;a:{r=void 0===r?Sh:r;for(l=0;l<r.length;++l)if(m=r[l],m instanceof Qh&&m.Xc(a)){r=new Pb(a,Qb);break a}r=void 0}r=r||Tb;if(r instanceof Pb)var w=Rb(r);else{b:if(Jh){try{w=new URL(r)}catch(t){w="https:";break b}w=w.protocol}else c:{w=document.createElement("a");try{w.href=r}catch(t){w=void 0;break c}w=
w.protocol;w=":"===w||""===w?"https:":w}w="javascript:"!==w?r:void 0}void 0!==w&&(c.href=w)}return!0}
;z("yt.setConfig",Rk);z("yt.config.set",Rk);z("yt.setMsg",Rs);z("yt.msgs.set",Rs);z("yt.logging.errors.log",ts);
z("writeEmbed",function(){var a=L("PLAYER_CONFIG");if(!a){var b=L("PLAYER_VARS");b&&(a={args:b})}lt(!0);"gvn"===a.args.ps&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});var c=document.referrer;b=L("POST_MESSAGE_ORIGIN");window!==window.top&&c&&c!==document.URL&&(a.args.loaderUrl=c);Eu();c=L("WEB_PLAYER_CONTEXT_CONFIGS").WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER;if(!c.serializedForcedExperimentIds){var d=ll(window.location.href);
d.forced_experiments&&(c.serializedForcedExperimentIds=d.forced_experiments)}Ex=Cx(a,c);Ex.addEventListener("onVideoDataChange",Hx);Ex.addEventListener("onReady",Jx);a=L("POST_MESSAGE_ID","player");L("ENABLE_JS_API")?Gx=new Kw(Ex):L("ENABLE_POST_API")&&"string"===typeof a&&"string"===typeof b&&(Fx=new Rw(window.parent,a,b),Gx=new Ow(Ex,Fx.connection));jw();M("ytidb_create_logger_embed_killswitch")||M("embeds_web_disable_nwl")||Bm();a={};ww||(ww=new vw);ww.install((a.flush_logs={callback:function(){Jr()}},
a));
M("embeds_web_disable_nwl")||yq();M("ytidb_clear_embedded_player")&&fi.S(function(){var e;if(!mv){var f=ir(),g={Gb:lv,vc:kv};f.h.set(g.Gb,g);g={Ub:{feedbackEndpoint:At(gv),modifyChannelNotificationPreferenceEndpoint:At(hv),playlistEditEndpoint:At(iv),subscribeEndpoint:At(ev),unsubscribeEndpoint:At(fv),webPlayerShareEntityServiceEndpoint:At(jv)}};var h=vt.getInstance(),l={};h&&(l.client_location=h);if(void 0===m){nt.h||(nt.h=new nt);var m=nt.h}void 0===e&&(e=f.resolve(lv));Su(g,e,m,l);m={Gb:Yu,wc:Ru.h};
f.h.set(m.Gb,m);mv=f.resolve(Yu)}Uv()})});
var Nx=bl(function(){Lu();mt();Cv.h||(Cv.h=new Cv);var a=Cv.h;var b=16623;var c=void 0===c?{}:c;Object.values(Ss).includes(b)||(us(new P("createClientScreen() called with a non-page VE",b)),b=83769);c.isHistoryNavigation||a.h.push({rootVe:b,key:c.key||""});a.o=[];a.v=[];c.Xb?Gv(a,b,c):Hv(a,b,c)}),Ox=bl(function(a){M("embeds_web_enable_load_player_from_page_show")&&!a.persisted&&(Lu(),mt())}),Px=bl(function(a){M("embeds_web_enable_dispose_player_if_page_not_cached_killswitch")?Kx():a.persisted||(M("embeds_web_enable_load_player_from_page_show")?
Kx():$c?setTimeout(function(){Kx()},0):Kx())}),Qx=bl(Kx);
window.addEventListener?(window.addEventListener("load",Nx),M("embeds_web_enable_load_player_from_page_show")?(window.addEventListener("pageshow",Ox),window.addEventListener("pagehide",Px)):$c?window.addEventListener("beforeunload",Px):window.addEventListener("pagehide",Px)):window.attachEvent&&(window.attachEvent("onload",Nx),window.attachEvent("onunload",Qx));z("yt.abuse.player.botguardInitialized",B("yt.abuse.player.botguardInitialized")||Yw);
z("yt.abuse.player.invokeBotguard",B("yt.abuse.player.invokeBotguard")||Zw);z("yt.abuse.dclkstatus.checkDclkStatus",B("yt.abuse.dclkstatus.checkDclkStatus")||kw);z("yt.player.exports.navigate",B("yt.player.exports.navigate")||Mx);z("yt.util.activity.init",B("yt.util.activity.init")||Nq);z("yt.util.activity.getTimeSinceActive",B("yt.util.activity.getTimeSinceActive")||Qq);z("yt.util.activity.setTimestamp",B("yt.util.activity.setTimestamp")||Oq);}).call(this);
