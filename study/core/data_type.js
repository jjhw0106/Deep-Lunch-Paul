// var user = {
// 	name: "Howon",
// 	gender: "male"
// }
 
// var changeName = function (user, newName) {
// 	return {
// 		name: newName,
// 		gender: user.gender
// 	}
// }

// var user2 = changeName(user, 'jung');

// if(user !== user2) {
// 	console.log('유저 정보가 변경되었습니다');
// }

// if(user != user2) {
// 	console.log(user.name, user2.name);
// 	console.log(user === user2);
// }

var copyObject = function(target) {
	var result = {};
	for (var prop in target){
		console.log("=====normal=====");
		console.log(prop);
		result [prop] = target[prop];
	}
	return result;
}

var copyObjectDeep = function(target) {
	var result = {};
	if (typeof target === 'object' && target !== null) {
		for(var prop in target) {
			console.log("=====deep=====");
			console.log(prop);
			result[prop] = copyObjectDeep(target[prop]);
		}
	} else {
		result = target;
	}
	return result;
}

// var user3 = copyObject(user);
// user3.name = 'jung';
// console.log(user3);

var user = {
	name: 'Jaenam',
	urls: {
		portfolio: 'http://github.com/abc',
		blog: 'http://blog.com',
		facebook: 'http://facebook.com/abc'
	}
}

var user2 = copyObject(user);
var user2 = copyObjectDeep(user);

user.urls.portfolio = 'http://portfolio.com';