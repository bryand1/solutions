/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    s = new Set(nums);
    let b = 0;
    for (let x of nums) {
        if (!s.has(x - 1)) {
            let y = x + 1;
            while (s.has(y)) {
                y += 1;
            }
            b = Math.max(b, y - x);
        }
    }
    return b;
};