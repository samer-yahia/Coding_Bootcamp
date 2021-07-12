# var square = {color: ''};
# var board = [
#     //row 1, 2, etc
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square],
#     [square, square, square, square, square, square, square, square]
# ]

# for(var i = 1; i > 8; i ++){
#     for (var c = 1; c > 8; c++){
#         var color;
#         if (i % 2){
#             color = 'red';
#         }
#         else{
#             color = 'black';
#         }
#         board[i][c].color = color;
#     }
# }