function move(event){
	console.log("Ferfect!");
	console.log(event.target)
	console.log(event.target.parentNode)

}



function init(){
	var ls = [
	"r1_c1","r1_c2","r1_c3","r1_c4","r1_c5","r1_c6","r1_c7","r1_c8",
	"r2_c1","r2_c2","r2_c3","r2_c4","r2_c5","r2_c6","r2_c7","r2_c8",
	"r7_c1","r7_c2","r7_c3","r7_c4","r7_c5","r7_c6","r7_c7","r7_c8",
	"r8_c1","r8_c2","r8_c3","r8_c4","r8_c5","r8_c6","r8_c7","r8_c8",
	];

	var corresp_pieces = [
		"rook_white","knight_white","bishop_white","king_white","queen_white","bishop_white","knight_white","rook_white",
		"pawn_white","pawn_white","pawn_white","pawn_white","pawn_white","pawn_white","pawn_white","pawn_white",
		"pawn_black","pawn_black","pawn_black","pawn_black","pawn_black","pawn_black","pawn_black","pawn_black",
		"rook_black","knight_black","bishop_black","king_black","queen_black","bishop_black","knight_black","rook_black",

	];

	var len = ls.length;

	for (var i=0;i<len;i++){
		var str = ls[i];
		//ra_cb
		var a = str.slice(0,2);
		var b = str.slice(3,5);
		console.log(str,a,b);
		document.getElementsByClassName(a)[0].getElementsByClassName(b)[0].style.backgroundImage = `url('${urls[corresp_pieces[i]]}')`;
		document.getElementsByClassName(a)[0].getElementsByClassName(b)[0].style.backgroundSize = "cover";
		posn[str] = corresp_pieces[i];	
	}

	var nodes =  document.getElementsByTagName('div')
	// nodes = nodes.filter(hasChildNodes)
	console.log(nodes)
	for(var i=0;i<nodes.length;i++){
		var cells = nodes[i].childNodes;
		for (var j = 0; j < cells.length; j++) {
			cells[j].onclick = function(event){move(event)};
		}
	}
	console.log(posn);

}



var urls = {};
var pieces = [
	"pawn_black",
	"pawn_white",
	"rook_black",
	"rook_white",
	"knight_black",
	"knight_white",
	"bishop_black",
	"bishop_white",
	"king_black",
	"king_white",
	"queen_black",
	"queen_white"
];

var len_pieces = pieces.length;
for (var i=0;i<len_pieces;i++){
	urls[pieces[i]] = "images/"+pieces[i] + ".svg";
}

var posn = {};
for (var i = 1;i<=8;i++){
	for(var j = 1;j<=8;j++){
		posn["r"+i+"_c"+j] = null;
	}
}

var active = 0;
var white_move = 1; //if its white move then this will be 1 else 0 . By default for now i am taking white goes first


//Need to Add the click events 

