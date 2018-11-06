const Mocha  = require('mocha');
const assert = require('assert');
const mocha  = new Mocha();
mocha.suite.emit('pre-require', this, 'solution', mocha);
// ^^^^^^^ ignore this ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

/*
 * Abbreviations (a11s)
 *
 * Implement an abbreviate() function.
 * It should abbreviate words in the following format:
 *
 * “accessibility” => “a11y”
 * “internationalization” => “i18n”
 * 
 */
function abbreviate(str) {

}


// Write some tests
describe('The abbreviate() function', function() {
  
  // A basic test case
  it('should return the abbreviated value', function() {
    assert.equal(abbreviate("accessibility"), "a11y");
    assert.equal(abbreviate("internationalization"), "i18n");
    assert.equal(abbreviate("Etsy"), "E2y");
  });
  
 
  
});


// This runs the tests
mocha.run();
