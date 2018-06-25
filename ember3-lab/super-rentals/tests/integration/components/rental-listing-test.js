import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';
import EmberObject from '@ember/object';

module('Integration | Component | rental-listing', function(hooks) {
    setupRenderingTest(hooks);

  hooks.beforeEach(function () {
    this.rental = EmberObject.create({
      image: 'fake.png',
      title: 'test-title',
      owner: 'test-owner',
      type: 'test-type',
      city: 'test-city',
      bedrooms: 3
    });
  });

    test('should display rental details', async function(assert) {
       await render(hbs`{{rental-listing rental=rental}}`);
    });

    test('should toggle wide class on click', async function(assert) {
       await render(hbs`{{rental-listing rental=rental}}`);
    });
});

  // test('it renders', async function(assert) {
  //   Set any properties with this.set('myProperty', 'value');
  //   Handle any actions with this.set('myAction', function(val) { ... });



  //   await render(hbs`{{rental-listing}}`);

  //   assert.equal(this.element.textContent.trim(), '');

  //   // Template block usage:
  //   await render(hbs`
  //     {{#rental-listing}}
  //       template block text
  //     {{/rental-listing}}
  //   `);

  //   assert.equal(this.element.textContent.trim(), 'template block text');
  // });
// });
