package colorizer

//K is blacK
var K = "\u001B[30m"

//R is Red
var R = "\u001B[31m"

//G is Green
var G = "\u001B[32m"

//Y is Yellow
var Y = "\u001B[33m"

//B is Blue
var B = "\u001B[34m"

//P is Purple
var P = "\u001B[35m"

//C is Cyan
var C = "\u001B[36m"

//W is White
var W = "\u001B[37m"

//Colorize colorizing text in console adding ANSI color codes
func Colorize(text string, color string) string {
	return color + text + "\u001B[0m"
}
