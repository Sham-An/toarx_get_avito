(function (c) {
    if (isEngineInited()){
        return;
    }

    let script = document.createElement('script');
    script.type = 'text/javascript';
    script.async = 1;
    script.src = c.managerUrl;
    script.dataset.roxotInited = 'true';

    let head = document.getElementsByTagName('head')[0];
    head.insertBefore(script, head.firstChild);

    window.rom = window.rom || {cmd: [], icmd: []};
    window.rom.icmd = window.rom.icmd || [];
    window.rom.icmd.push(c);

    function isEngineInited(){
        return  document.querySelectorAll('[data-roxot-inited]').length;
    }
})({"publisherId":"c427193e-c45c-4b31-b9de-0d5bc41115fd","publisher":"TechMedia","adBlockMode":"iframe","iframeSspList":["google","prebid","prebid_dfp"],"managerUrl":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/common-engine.js?v=s-4da7301e-846c-497a-bc91-a3814647ef3b","wrapperUrl":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/wrapper.js?v=s-4da7301e-846c-497a-bc91-a3814647ef3b","placementConfigTemplate":"https:\/\/cdn.skcrtxr.com\/wrapper-builder\/placement\/__PLACEMENT_ID__?v=d-1661436269","gfsPlacementOptionsTemplate":"https:\/\/cdn.skcrtxr.com\/wrapper-builder\/gfs-placement\/__PLACEMENT_ID__?v=d-1661436269","isLanguageSpecific":true,"hostConfig":{"habr.com":{"wrapperOptions":[],"isAcceptableAdsEnabled":false}},"isBrowserSpecific":false,"isOsSpecific":false,"isDeviceTypeSpecific":false,"isGeoSpecific":false,"isGetParamSpecific":false,"dynamicUrlTemplate":"","wrapperConfig":{"monetizationStatsIntegration":{"enabled":true,"requestSettings":{"isNeedToSend":true,"sampleCoefficient":1},"impressionSettings":{"isNeedToSend":true,"sampleCoefficient":1}},"host":"habr.com","engineFileName":"common-engine.js","enableAdFirstLoadInHiddenTab":true,"universalPlaceHolder":{"enabled":false},"prebid":{"prebidTimeout":1500,"adjustment":{"adriver":1,"appnexus":0.95,"between":1,"criteo":0.9,"getintent":0.06,"mytarget":0.1,"otm":0.96,"rtbhouse":1,"rubicon":0.98},"path":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/prebid.js?v=s-4da7301e-846c-497a-bc91-a3814647ef3b"},"adfox":{"hb":{"biddersMap":{"betweenDigital":"1945468","myTarget":"1945461","otm":"1945469","segmento":"1945470","getintent":"1945477","hybrid":"1945478","adriver":"1945479","buzzoola":"1945480","relap":"1945481","adfox_yandex_premium-publisher-network":"1946302","mts":"2030417","mediasniper":"2032962","rtbhouse":"1393902","criteo":"1393905","videonow":"1407059"},"timeout":1000}},"prebidAnalyticsIntegration":{"enabled":true,"publisherId":"92707dda-5614-4d3a-b4f5-531645d13ecf","auctionSettings":{"isNeedToSend":false,"sampleCoefficient":10},"impressionSettings":{"isNeedToSend":true,"sampleCoefficient":10}},"roxotYaMetric":{"enabled":true,"counterId":88477929},"videojsLibs":{"path":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/video-libs.js?v=s-4da7301e-846c-497a-bc91-a3814647ef3b"},"pageUrlVariableName":"roxotPlusPageUrl","stubVideoPath":"https:\/\/cdn.skcrtxr.com\/wrapper\/js\/video-ad?v=s-4da7301e-846c-497a-bc91-a3814647ef3b","adfoxIntegrationType":"direct","yandexIntegrationType":"common"},"lazyLoading":[],"geoSpecificUrl":"https:\/\/skcrtxr.com\/geo\/api\/region\/c427193e-c45c-4b31-b9de-0d5bc41115fd"})