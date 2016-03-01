import Ember from 'ember';

export function hCode(content/*, hash*/) {
    let rcontent = Ember.$.trim(content);
    return Ember.String.htmlSafe(rcontent);
}

export default Ember.Helper.helper(hCode);