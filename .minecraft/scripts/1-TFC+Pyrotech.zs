var masonryBrick = <pyrotech:material:16>;
var tarredBoard = <pyrotech:material:23>;
var durableTwine = <pyrotech:material:26>;
var rawWool = <tfc:animal/product/wool>;
var mediumRawHide = <tfc:hide/raw/medium>;

var twine = <ore:twine>;
var leather = <ore:leather>;
var ingotAnyBronze = <ore:ingotAnyBronze>;

recipes.remove(<pyrotech:bag_simple>);
recipes.remove(<pyrotech:bag_durable>);

// Rock Bag -> Durable Rock Bag (retaining NBT!)
recipes.addShaped("rock_bag_conversion", <pyrotech:bag_durable>,
										 [[tarredBoard, durableTwine, tarredBoard], 
										  [durableTwine, <pyrotech:bag_simple>.marked("CarryOverNBT"), durableTwine], 
										  [masonryBrick, durableTwine, masonryBrick]],
										  function(out, ins, cInfo) {
											  return out.updateTag(ins.CarryOverNBT.tag);
										  }, null);

recipes.addShaped("simple_rock_bag", <pyrotech:bag_simple>, [[rawWool, twine, rawWool], [mediumRawHide, <pyrotech:stash>, mediumRawHide], [rawWool, mediumRawHide, rawWool]]);
recipes.addShaped("durable_rock_bag", <pyrotech:bag_durable>, [[leather, durableTwine, leather], [leather, <pyrotech:stash_stone>, leather], [leather, ingotAnyBronze, leather]]);