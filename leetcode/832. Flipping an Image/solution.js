var flipAndInvertImage = function(A) {
    return A.map(row => row.reverse().map(num => num^1));
};
