import Ember from 'ember';

const {
    computed,
    Handlebars: {
        Utils
    },
    String: {
        htmlSafe
    }
} = Ember;

Ember.Handlebars.Utils.escapeExpression

export default Ember.Component.extend({
    didInsertElement(){
        this._super(...arguments);
        // hljs.highlightBlock(this.$('pre code'));
        hljs.initHighlightingOnLoad()
    },
    codeBlock: computed('code', {
        get(){
            let code = Utils.escapeExpression(this.attrs.code);
            return htmlSafe(code);
        }
    })
})