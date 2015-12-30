var _String__escapeChars = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;'
};

function _String__escapeReplace(c) {
    return _String__escapeChars[c];
}

/* exported String__escape */
function String__escape(str) {
    return  typeof str == 'string' ?
                str.replace(/[&<>"]/g, _String__escapeReplace) :
                str == undefined ? '' : str;
}

/* exported String__nl2br */
function String__nl2br(str) {
    return  typeof str == 'string' ?
                str.replace(/\r\n|\n\r|\r|\n/g, '<br>') :
                str == undefined ? '' : str;
}

/* exported String__parseQuery */
function String__parseQuery(query) {
    var ret = {},
        vars = query.split('&'),
        i,
        pair;

    for (i = 0; i < vars.length; i++) {
        if (vars[i]) {
            pair = vars[i].split('=');
            ret[decodeURIComponent(pair[0])] = decodeURIComponent(pair[1] || '');
        }
    }

    return ret;
}

/* exported String__param */
function String__param(data, url) {
    var ret = '',
        i;

    Object__each(data, function(key, value) {
        if (value != undefined) {
            if (value instanceof Array) {
                for (i = 0; i < value.length; i++) {
                    ret += '&' + encodeURIComponent(key) + '=' + encodeURIComponent(value[i]);
                }
            } else {
                ret += '&' + encodeURIComponent(key) + '=' + encodeURIComponent(value);
            }
        }
    });

    return url ? (url + ret).replace(/[&?]{1,2}/, '?') : ret.substr(1);
}

/* exported String__repeat */
function String__repeat(str, n) {
    return Array(n + 1).join(str);
}

/* exported String__random */
function String__random(possible, len) {
    var ret = '',
        i;

    for (i = 0; i < len; i++) {
        ret += possible[Math.floor(Math.random() * possible.length)];
    }

    return ret;
}