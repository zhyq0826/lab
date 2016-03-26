import Ember from 'ember';
import config from './config/environment';


const {
  inject: { service },
  run: { scheduleOnce },
  getWithDefault,
  get
} = Ember;

var Router = Ember.Router.extend({
  location: config.locationType,

  didTransition() {
    this._super(...arguments);
    this._trackPage();
  },
  _trackPage(){
    scheduleOnce('afterRender', this, () => {
      const page = document.location.pathname;
      const title = getWithDefault(this, 'currentRouteName', 'unknown');
      Ember.Logger.info(`${page} ${title}`);
    });
  }
});

Router.map(function() {
    this.route('ember-easy-orm', function(){
      this.route('form');
    });

    this.route('ember-semantic-ui');
    this.route('demo-action', function(){
        
    });
    this.route('ui-date-input');
});

export default Router;
