/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    var stack = [-1,];
    var r = 0;
    for (var i = 0; i < s.length; i++) {
        if (s.charAt(i) === '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i);
            } else {
                r = Math.max(r, i - stack[stack.length - 1]);
            }
        }
    }
    return r;
};
