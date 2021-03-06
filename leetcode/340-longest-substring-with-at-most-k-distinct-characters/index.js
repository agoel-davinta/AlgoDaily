/*
    1st: 2pointers + hashtable
    - similar to lc3, 159, 904
    - maintain the sliding window to have k unique keys

    Time    O(N)
    Space   O(N)
    148 ms, faster than 15.16%
*/
var lengthOfLongestSubstringKDistinct = function (s, k) {
	let ht = {};
	let slow = 0;
	let res = 0;
	for (let i = 0; i < s.length; i++) {
		const x = s[i];

		if (x in ht) {
			ht[x] += 1;
		} else {
			ht[x] = 1;
		}

		while (Object.keys(ht).length > k) {
			const last = s[slow];
			ht[last] -= 1;
			slow += 1;
			if (ht[last] == 0) {
				delete ht[last];
			}
		}
		res = Math.max(res, i - slow + 1);
	}
	return res;
};
