def abbreviate_single(st):
    
    n = len(st)
    
    if n < 4:
        return st
    
    repit = n-2
    
    return st[0] + str(repit) + st[-1]


def abbreviate(st):
    
    l = st.split()
    output = []
    
    for e in l:
        output.append(abbreviate_single(e))
        
    return " ".join(output)   
        

print(abbreviate("keep commerce human"))
print(abbreviate("code as craft"))

# print(abbreviate("accessibility"))
# print(abbreviate("internationalization"))
# print(abbreviate("Etsy"))
# print(abbreviate("dog"))

# assert abbreviate("Etsy")=="E2y", "True"

# assert.equal(abbreviate("keep commerce human"), "k2p c6e h3n");
# assert.equal(abbreviate("code as craft"), "c2e as c3t");

# 
# Your previous JavaScript content is preserved below:
# 
# const Mocha  = require('mocha');
# const assert = require('assert');
# const mocha  = new Mocha();
# mocha.suite.emit('pre-require', this, 'solution', mocha);
# // ^^^^^^^ ignore this ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# 
# /*
#  * Abbreviations (a11s)
#  *
#  * Implement an abbreviate() function.
#  * It should abbreviate words in the following format:
#  *
#  * “accessibility” => “a11y”
#  * “internationalization” => “i18n”
#  * 
#  */
# function abbreviate(str) {
# 
# }
# 
# 
# // Write some tests
# describe('The abbreviate() function', function() {
#   
#   // A basic test case
#   it('should return the abbreviated value', function() {
#     assert.equal(abbreviate("accessibility"), "a11y");
#     assert.equal(abbreviate("internationalization"), "i18n");
#     assert.equal(abbreviate("Etsy"), "E2y");
#     assert.equal(abbreviate("Ey"), "Ey");
#     assert.equal(abbreviate("dog"), "dog");
#   });
#   
#  
#   
# });
# 
# 
# // This runs the tests
# mocha.run();

