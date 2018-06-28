import Component from '@ember/component';

// Another way to say this is that the value property of input is bound to the value property of the component. 
// If the property changes, either by the user typing in the input field, 
// or by assigning a new value to it in our program, 
// the new value of the property is present in both the rendered web page and in the code.
export default Component.extend({
    classNames: ['list-filter'],
    value: '',
    init() {
        this._super(...arguments);
        // this.get('filter')('').then((results) => this.set('results', results));
        this.get('filter')('').then((allResults) => {
            this.set('results', allResults.results);
        });
    },

    actions: {
        handleFilterEntry() {
            let filterInputValue = this.get('value');
            let filterAction = this.get('filter');
            // filterAction(filterInputValue).then((filterResults) => this.set('results', filterResults));
            filterAction(filterInputValue).then((filterResults) => {
                if (filterResults.query === this.get('value')) {
                    this.set('results', filterResults.results);
                }
            });
        }
    }
});