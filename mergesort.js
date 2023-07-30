var merge = function(s, low, middle, high) {
    var i;
    var buffer1 = [];
    var buffer2 = [];

    for (i = low; i <= middle; i++) buffer1.push(s[i]);
    for (i = middle + 1; i <= high; i++) buffer2.push(s[i]);

    i = low;
    while (!(buffer1.length == 0 || buffer2.length == 0)) {
        console.log("comparing " + buffer1[0] + ", " + buffer2[0])
        if (buffer1[0] <= buffer2[0]) {
            console.log("buffer1: " + buffer1);
            console.log("buffer2: " + buffer2);
            console.log("changing array[" + (i + 1) + "]");
            s[i++] = buffer1.shift();
            console.log("s:" + s);
        } else {
            console.log("buffer1: " + buffer1);
            console.log("buffer2: " + buffer2);
            s[i++] = buffer2.shift();
            console.log("s:" + s);
        }
        console.log('----')
    }

    while (!(buffer1.length == 0)) s[i++] = buffer1.shift()
    while (!(buffer2.length == 0)) s[i++] = buffer2.shift()
}

var mergesort = function(s, low, high) {
    var i;
    var middle;

    if (low < high) {
        middle = Math.floor((low + high) / 2);
        mergesort(s, low, middle);
        mergesort(s, middle + 1, high);
        merge(s, low, middle, high);
    }
}


arr1 = [4, 4, 6, 9, 1, 5, 3, 2, 7];
console.log(arr1)
//merge(arr1, 0, Math.floor(arr1.length/2), arr1.length - 1);
mergesort(arr1, 0, arr1.length - 1);
console.log(arr1)
