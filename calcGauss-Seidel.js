function Seidel_Gauss(newX,oldX){
    var result = Math.abs(((newX - oldX)/newX) * 100)
    return result
}

var x1 = Seidel_Gauss(48.4375, 51.25)
var x2 = Seidel_Gauss(-57.1875, 5.625)
var x3 = Seidel_Gauss(-102.65625, 128.4375)
console.log("X1 = ", x1)
console.log("X2 = ", x2)
console.log("X3 = ", x3)