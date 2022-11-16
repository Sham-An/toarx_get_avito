var extend = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
	hasProp = {}.hasOwnProperty,
	slice = [].slice;

(function(w, d, b) {
	var CROSS_VERSION_COMPATIBILITY, CURRENT_VERSION, LIBRARY_TYPE, ShowjetPlugin, test;
	CROSS_VERSION_COMPATIBILITY = {
		OLD: {
			GET_MODULE: function() {
				return b.Common.Modules.Base.BaseModule;
			},
			CREATIVE: {
				EXTEND: function() {
					b.Utils.extend(this.core.loadedData, {
						contentType: "vpaid",
						content: {
							mimeType: "application/javascript"
						},
						title: "",
						description: "",
						sponsorName: "",
						sponsorLogo: ""
					});
				},
				GET_DATA: function() {
					return this.core.loadedData;
				}
			},
			WIDGET: {
				PATH: "Buzzplayer.Widgets.Player.Core",
				CREATE_PLAYER: function() {
					new b.Buzzplayer.Plugins.ShowjetPlayer(this.core);
					this.callStrategy("widget:loadVideo");
				}
			},
			EVENTS: {},
			STRATEGIES: {}
		},
		NEW: {
			GET_MODULE: function() {
				return b.Shared.Modules.Base.Submodule;
			},
			CREATIVE: {
				EXTEND: function() {
					b.Utils.extend(this.node.loadedData, {
						title: "",
						description: "",
						sponsorName: "",
						sponsorLogo: ""
					});
					b.Utils.extend(this.node.loadedData.content.widgets[0], {
						isVPAIDJSVideo: true
					});
				},
				GET_DATA: function() {
					return this.node.loadedData;
				}
			},
			WIDGET: {
				PATH: "Buzzplayer.Widgets.Player.Widget",
				CREATE_PLAYER: function() {
					b.Utils.initModules(this, ["ShowjetPlayer"], "Buzzplayer.Plugins");
					this.callStrategy("widget:load_video");
				}
			},
			EVENTS: {
				"vpaidjs:adStarted": "vpaidjs:ad_started",
				"vpaidjs:adVideoStart": "vpaidjs:ad_video_start",
				"vpaidjs:adImpression": "vpaidjs:ad_impression",
				"vpaidjs:adVideoFirstQuartile": "vpaidjs:ad_video_first_quartile",
				"vpaidjs:adVideoMidpoint": "vpaidjs:ad_video_midpoint",
				"vpaidjs:adVideoThirdQuartile": "vpaidjs:ad_video_third_quartile",
				"vpaidjs:adVideoComplete": "vpaidjs:ad_video_complete"
			},
			STRATEGIES: {
				"api:sendEvent": "api:send_event",
				"resize:calcHeight": "resize:calc_height"
			}
		}
	};
	try {
		test = Buzzoola.Shared.Modules.Base.Node;
		LIBRARY_TYPE = "NEW";
	} catch (error) {
		LIBRARY_TYPE = "OLD";
	}
	CURRENT_VERSION = CROSS_VERSION_COMPATIBILITY[LIBRARY_TYPE];
	ShowjetPlugin = (function(superClass) {
		var ref;

		extend(ShowjetPlugin, superClass);

		function ShowjetPlugin() {
			return ShowjetPlugin.__super__.constructor.apply(this, arguments);
		}

		ShowjetPlugin.prototype.addsStrategies = [[(ref = CURRENT_VERSION.STRATEGIES["resize:calcHeight"]) != null ? ref : "resize:calcHeight", 999999, "calcHeight"]];

		ShowjetPlugin.prototype.handlesEvents = {
			"core:ads_loaded": function() {
				this.core.params.behavior = "video";
			}
		};

		ShowjetPlugin.prototype.wrapperUrl = null;

		ShowjetPlugin.prototype.init = function() {
			var data;
			data = CURRENT_VERSION.CREATIVE.GET_DATA.call(this);
			this.wrapperUrl = data.jsWrapperUrl;
			CURRENT_VERSION.CREATIVE.EXTEND.call(this);
			this.initMixin();
			this.trigger("remote_module_ready");
		};

		ShowjetPlugin.prototype.calcHeight = function() {
			var args, height, ref1, ref2;
			args = 1 <= arguments.length ? slice.call(arguments, 0) : [];
			if (LIBRARY_TYPE === "OLD") {
				this.core.loadedData.jsWrapperUrl = "";
			}
			height = (ref2 = this.core).callStrategyByMaxWeight.apply(ref2, [(ref1 = CURRENT_VERSION.STRATEGIES["resize:calcHeight"]) != null ? ref1 : "resize:calcHeight", 999000].concat(slice.call(args)));
			if (LIBRARY_TYPE === "OLD") {
				this.core.loadedData.jsWrapperUrl = this.wrapperUrl;
			}
			return height;
		};

		ShowjetPlugin.prototype.initMixin = function() {
			var self;
			self = this;
			return this.core.setMixin(CURRENT_VERSION.WIDGET.PATH, function(Core) {
				var PlayerCore;
				PlayerCore = (function(superClass1) {
					extend(PlayerCore, superClass1);

					function PlayerCore() {
						return PlayerCore.__super__.constructor.apply(this, arguments);
					}

					PlayerCore.prototype.embedMediaPlayer = function() {
						var args, data;
						args = 1 <= arguments.length ? slice.call(arguments, 0) : [];
						data = CURRENT_VERSION.CREATIVE.GET_DATA.call(this);
						if (data.jsWrapperUrl === self.wrapperUrl) {
							if (!b.Buzzplayer.Plugins.ShowjetPlayer) {
								self.initPlayerClass();
							}
							CURRENT_VERSION.WIDGET.CREATE_PLAYER.call(this);
							this.trigger("widget:embeded");
						} else {
							PlayerCore.__super__.embedMediaPlayer.apply(this, args);
						}
					};

					return PlayerCore;

				})(Core);
				return PlayerCore;
			});
		};

		ShowjetPlugin.prototype.initPlayerClass = function() {
			var ShowjetPlayer;
			ShowjetPlayer = (function(superClass1) {
				var ref1;

				extend(ShowjetPlayer, superClass1);

				function ShowjetPlayer() {
					return ShowjetPlayer.__super__.constructor.apply(this, arguments);
				}

				ShowjetPlayer.prototype.addsStrategies = [[(ref1 = CURRENT_VERSION.STRATEGIES["api:sendEvent"]) != null ? ref1 : "api:sendEvent", 999999, "sendEvent"]];

				ShowjetPlayer.prototype.handlesEvents = {
					"before:destroyed": function() {
						this.destroy();
					}
				};

				ShowjetPlayer.prototype.events = null;

				ShowjetPlayer.prototype.maxId = 0;

				ShowjetPlayer.prototype.preventComplete = false;

				ShowjetPlayer.prototype.destroyed = false;

				ShowjetPlayer.prototype.init = function() {
					var args, content, data, domain, ref2, ref3, ref4, sjuid, volume;
					args = 1 <= arguments.length ? slice.call(arguments, 0) : [];
					ShowjetPlayer.__super__.init.apply(this, args);
					data = CURRENT_VERSION.CREATIVE.GET_DATA.call(this);
					content = data.content;
					volume = !!data.autoPlay ? 0 : 500;
					sjuid = parseInt((ref2 = content.sjuid) != null ? ref2 : null, 10);
					if (isNaN(sjuid)) {
						sjuid = 257;
					}
					domain = (ref3 = content.domain) != null ? ref3 : "https://showjet.net";
					this.iframeUrl = domain + "/promolanding?autoplay=true&sjuid2=1&sjuid5=" + sjuid + "&sjuid1=10&sjuid6=" + volume + "&sjuid7=true";
					this.currentTime = -1;
					this.totalTime = (ref4 = data.duration) != null ? ref4 : 100;
					this.events = {};
				};

				ShowjetPlayer.prototype._onMessage = function(event) {
					var data;
					data = event.data;
					if (event.source === this.iframe.contentWindow && b.Utils.isString(data) && data.indexOf('sj_') !== -1) {
						this.iframeHandler(data);
					}
				};

				ShowjetPlayer.prototype.handleIframeMessage = function(event) {
					var ref10, ref2, ref3, ref4, ref5, ref6, ref7, ref8, ref9, strategy;
					this.core.log("SHOWJET --> BUZZ: POST MESSAGE", event);
					if (this.destroyed) {
						this.core.log("BUZZ: POST MESSAGE FOR DESTROYED PLAYER");
						return;
					}
					switch (event) {
						case "sj_no_ads":
							this.trigger("error", "nobanner probably");
							break;
						case "sj_has_ads":
							setTimeout((function(_this) {
								return function() {
									return _this.changeState("ready");
								};
							})(this), 3000);
							break;
						case "sj_adStarted":
							if (this.events.start > 0) {
								strategy = (ref2 = CURRENT_VERSION.STRATEGIES["api:sendEvent"]) != null ? ref2 : "api:sendEvent";
								this.callStrategy(strategy, "ctor", 0);
								this.callStrategy(strategy, "player_seen", 0);
							}
							this.handleStateChange("playing");
							this.trigger((ref3 = CURRENT_VERSION.EVENTS["vpaidjs:adStarted"]) != null ? ref3 : "vpaidjs:adStarted");
							this.trigger((ref4 = CURRENT_VERSION.EVENTS["vpaidjs:adVideoStart"]) != null ? ref4 : "vpaidjs:adVideoStart");
							break;
						case "sj_impression":
							this.trigger((ref5 = CURRENT_VERSION.EVENTS["vpaidjs:adImpression"]) != null ? ref5 : "vpaidjs:adImpression");
							break;
						case "sj_ads_finished":
							this.preventComplete = true;
							this.changeState("finish");
							break;
						case "sj_player_error":
							this.trigger("error", "showjet video error");
							break;
						case "sj_adview25":
							this.trigger((ref6 = CURRENT_VERSION.EVENTS["vpaidjs:adVideoFirstQuartile"]) != null ? ref6 : "vpaidjs:adVideoFirstQuartile");
							break;
						case "sj_adview50":
							this.trigger((ref7 = CURRENT_VERSION.EVENTS["vpaidjs:adVideoMidpoint"]) != null ? ref7 : "vpaidjs:adVideoMidpoint");
							break;
						case "sj_adview75":
							this.trigger((ref8 = CURRENT_VERSION.EVENTS["vpaidjs:adVideoThirdQuartile"]) != null ? ref8 : "vpaidjs:adVideoThirdQuartile");
							break;
						case "sj_adview100":
							this.trigger((ref9 = CURRENT_VERSION.EVENTS["vpaidjs:adVideoComplete"]) != null ? ref9 : "vpaidjs:adVideoComplete");
							break;
						case "sj_skipped":
							this.core.destroy();
							break;
						case "sj_adclicked":
							this.callStrategy((ref10 = CURRENT_VERSION.STRATEGIES["api:sendEvent"]) != null ? ref10 : "api:sendEvent", "click", 0);
							break;
						case "sj_adpaused":
							this.handleStateChange("paused");
							break;
						case "sj_adresumed":
							this.handleStateChange("playing");
					}
				};

				ShowjetPlayer.prototype.handleStateChange = function(state) {
					switch (state) {
						case "playing":
							this.callStrategy("resize:call");
							if (!this.data.started) {
								this.data.started = true;
								setTimeout((function(_this) {
									return function() {
										_this.changeState("start");
										_this.changeState("duration");
										return _this.changeState("play");
									};
								})(this), 150);
							} else {
								this.changeState("play");
							}
							break;
						case "paused":
							this.changeState("pause");
					}
				};

				ShowjetPlayer.prototype.loadVideo = function() {
					var i, key, len, ref2;
					this.iframe = this.createIframe(this.iframeUrl, this.core.widgetDiv);
					ref2 = ["webkitAllowFullScreen", "mozallowfullscreen", "allowfullscreen"];
					for (i = 0, len = ref2.length; i < len; i++) {
						key = ref2[i];
						this.iframe.setAttribute(key, "");
					}
					this.resize(this.initialWidth, this.initialHeight);
				};

				ShowjetPlayer.prototype.getCurrentTime = function() {
					return this.currentTime;
				};

				ShowjetPlayer.prototype.getTotalTime = function() {
					return this.totalTime;
				};

				ShowjetPlayer.prototype.play = function() {
					this.core.log("BUZZ --> SHOWJET: POSTMESSAGE", "sj_adresume (play)");
					this.sendPostMessage("sj_adresume");
				};

				ShowjetPlayer.prototype.pause = function() {
					if (!this.data.started) {
						return;
					}
					this.core.log("BUZZ --> SHOWJET: POSTMESSAGE", "sj_adpause (pause)");
					this.sendPostMessage("sj_adpause");
				};

				ShowjetPlayer.prototype.setVolume = function() {
					this.core.warn("setVolume is not implemented");
				};

				ShowjetPlayer.prototype.stop = function() {
					this.core.log("BUZZ --> SHOWJET: POSTMESSAGE", "sj_close (stop)");
					this.sendPostMessage("sj_close");
				};

				ShowjetPlayer.prototype.resize = function(width, height) {
					if (this.iframe) {
						this.iframe.setAttribute("style", "width: " + width + "px !important; height: " + height + "px !important");
						this.iframe.setAttribute("width", width);
						this.iframe.setAttribute("height", height);
					} else {
						this.initialWidth = width;
						this.initialHeight = height;
					}
				};

				ShowjetPlayer.prototype.sendEvent = function() {
					var args, base, data, event, params, ref2, ref3, ref4, seq, time;
					args = 1 <= arguments.length ? slice.call(arguments, 0) : [];
					if (args.length > 2 || !isNaN(args[1])) {
						event = args[0], time = args[1], params = args[2];
					} else {
						event = args[0], params = args[1];
					}
					if (params == null) {
						params = {};
					}
					if (event === "complete" && this.preventComplete) {
						return;
					}
					if (params.slugname || params.slug) {
						seq = Math.max(0, ((ref2 = this.events.ctor) != null ? ref2 : 0) - 1);
					} else {
						if ((base = this.events)[event] == null) {
							base[event] = 0;
						}
						seq = this.events[event]++;
					}
					if (seq > this.maxId) {
						this.maxId = seq;
						data = CURRENT_VERSION.CREATIVE.GET_DATA.call(this);
						if ((ref3 = data.extra) != null) {
							ref3.seqMarker = seq;
						}
					}
					this.core.callStrategyByMaxWeight((ref4 = CURRENT_VERSION.STRATEGIES["api:sendEvent"]) != null ? ref4 : "api:sendEvent", 999000, event, b.Utils.extend(params != null ? params : {}, {
						seqMarker: this.maxId
					}));
				};

				ShowjetPlayer.prototype.destroy = function() {
					this.destroyed = true;
					if (this.iframe == null) {
						return;
					}
					if (this.core.widgetDiv) {
						this.core.widgetDiv.removeChild(this.iframe);
					}
					return this.stop();
				};

				return ShowjetPlayer;

			})(b.Common.Mixins.Iframe(b.Buzzplayer.Widgets.Player.Modules.BaseVideoPlayer));
			b.Utils.addModule("Buzzplayer.Plugins.ShowjetPlayer", ShowjetPlayer);
		};

		return ShowjetPlugin;

	})(CURRENT_VERSION.GET_MODULE());
	return b.Utils.addModule("Buzzplayer.Plugins.branding_2022_03_01_sj", ShowjetPlugin);
}).call({}, window, document, Buzzoola);