#FLM: PUA to UMS

# Version 1.0

# Description:
# Generates composite glyphs in Unicode ranges 'Miscellaneous Symbols'
# and 'Musical Symbols' (UMS) from identical glyphs in the Private 
# User Area (PUA) range of a SMuFL font.

# Any preexisting glyphs in the UMS ranges are automatically skipped.

# version 1.0 does not generate glyphs in 'Medieval and 
# Renaissance', 'Daseian notation' or 'Chord diagrams' ranges.

# CAUTION! 
# Script will decompose any components in the reference glyphs
# prior to generating new glyphs.


# Credits:
# Knut Nergaard


print "Starting ..."

from FL import *

# List of glyphs to generate 
genDict = {
'uniE260': 'uni266D', 
'uniE261': 'uni266E', 
'uniE262': 'uni266F',
'uniE030': 'u1D100', 'uniE031': 'u1D101', 'uniE032': 'u1D102',
'uniE033': 'u1D103', 'uniE036': 'u1D104', 'uniE038': 'u1D105',
'uniE040': 'u1D106', 'uniE041': 'u1D107', 'uniE043': 'u1D108',
'uniE045': 'u1D109', 'uniE046': 'u1D10A', 'uniE047': 'u1D10B',
'uniE048': 'u1D10C', 'uniE101': 'u1D10D', 'uniE500': 'u1D10E',
'uniE501': 'u1D10F', 'uniE4C0': 'u1D110', 'uniE4C1': 'u1D111',
'uniE4CE': 'u1D112', 'uniE4D1': 'u1D113', 'uniE000': 'u1D114',
'uniE002': 'u1D115', 'uniE010': 'u1D116', 'uniE011': 'u1D117',
'uniE012': 'u1D118', 'uniE013': 'u1D119', 'uniE014': 'u1D11A',
'uniE015': 'u1D11B', 'uniE050': 'u1D11E', 'uniE053': 'u1D11F',
'uniE052': 'u1D120', 'uniE05C': 'u1D121', 'uniE062': 'u1D122',
'uniE065': 'u1D123', 'uniE064': 'u1D124', 'uniE069': 'u1D125',
'uniE06A': 'u1D126', 'uniE263': 'u1D12A', 'uniE264': 'u1D12B',
'uniE270': 'u1D12C', 'uniE271': 'u1D12D', 'uniE272': 'u1D12E',
'uniE273': 'u1D12F', 'uniE274': 'u1D130', 'uniE275': 'u1D131',
'uniE47E': 'u1D132', 'uniE47F': 'u1D133', 'uniE08A': 'u1D134',
'uniE08B': 'u1D135', 'uniE511': 'u1D136', 'uniE51C': 'u1D137',
'uniE515': 'u1D138', 'uniE51D': 'u1D139', 'uniE4E2': 'u1D13A',
'uniE4E3': 'u1D13B', 'uniE4E4': 'u1D13C', 'uniE4E5': 'u1D13D',
'uniE4E6': 'u1D13E', 'uniE4E7': 'u1D13F', 'uniE4E8': 'u1D140',
'uniE4E9': 'u1D141', 'uniE4EA': 'u1D142', 'uniE0A9': 'u1D143',
'uniE0AF': 'u1D144', 'uniE0B3': 'u1D145', 'uniE0B8': 'u1D146',
'uniE0B9': 'u1D147', 'uniE0BD': 'u1D148', 'uniE0BE': 'u1D149',
'uniE0BF': 'u1D14A', 'uniE0C0': 'u1D14B', 'uniE0C1': 'u1D14C',
'uniE0C2': 'u1D14D', 'uniE0C6': 'u1D14E', 'uniE0C7': 'u1D14F',
'uniE0C8': 'u1D150', 'uniE0C9': 'u1D151', 'uniE0CA': 'u1D152',
'uniE0CB': 'u1D153', 'uniE0CC': 'u1D154', 'uniE0CD': 'u1D155',
'uniE0CE': 'u1D156', 'uniE0A3': 'u1D157', 'uniE0A4': 'u1D158',
'uniE0A5': 'u1D159', 'uniE120': 'u1D15A', 'uniE121': 'u1D15B',
'uniE1D0': 'u1D15C', 'uniE1D2': 'u1D15D', 'uniE1D3': 'u1D15E',
'uniE1D5': 'u1D15F', 'uniE1D7': 'u1D160', 'uniE1D9': 'u1D161',
'uniE1DB': 'u1D162', 'uniE1DD': 'u1D163', 'uniE1DF': 'u1D164',
'uniE210': 'u1D165', 'uniE211': 'u1D166', 'uniE220': 'u1D167',
'uniE221': 'u1D168', 'uniE222': 'u1D169', 'uniE225': 'u1D16A',
'uniE226': 'u1D16B', 'uniE227': 'u1D16C', 'uniE1E7': 'u1D16D',
'uniE240': 'u1D16E', 'uniE242': 'u1D16F', 'uniE244': 'u1D170',
'uniE246': 'u1D171', 'uniE248': 'u1D172', 'uniE8E0': 'u1D173',
'uniE8E1': 'u1D174', 'uniE8E2': 'u1D175', 'uniE8E3': 'u1D176',
'uniE8E4': 'u1D177', 'uniE8E5': 'u1D178', 'uniE8E6': 'u1D179',
'uniE8E7': 'u1D17A', 'uniE4A0': 'u1D17B', 'uniE4A2': 'u1D17C',
'uniE4A4': 'u1D17D', 'uniE4A6': 'u1D17E', 'uniE4AC': 'u1D17F',
'uniE4AE': 'u1D180', 'uniE4B0': 'u1D181', 'uniE4B2': 'u1D182',
'uniE634': 'u1D183', 'uniE635': 'u1D184', 'uniE5D4': 'u1D185',
'uniE5D7': 'u1D186', 'uniE5E1': 'u1D187', 'uniE5E2': 'u1D188',
'uniE5E3': 'u1D189', 'uniE5F0': 'u1D18A', 'uniE5F2': 'u1D18B',
'uniE523': 'u1D18C', 'uniE524': 'u1D18D', 'uniE525': 'u1D18E',
'uniE520': 'u1D18F', 'uniE521': 'u1D190', 'uniE522': 'u1D191',
'uniE52E': 'u1D192', 'uniE53F': 'u1D193', 'uniE560': 'u1D194',
'uniE562': 'u1D195', 'uniE566': 'u1D196', 'uniE567': 'u1D197',
'uniE568': 'u1D198', 'uniE569': 'u1D199', 'uniE56A': 'u1D19A',
'uniE594': 'u1D19B', 'uniE59D': 'u1D19C', 'uniE59E': 'u1D19D',
'uniE5A1': 'u1D19E', 'uniE5A7': 'u1D19F', 'uniE59F': 'u1D1A0',
'uniE59B': 'u1D1A1', 'uniE593': 'u1D1A2', 'uniE5A5': 'u1D1A3',
'uniE599': 'u1D1A4', 'uniE591': 'u1D1A5', 'uniE860': 'u1D1A6',
'uniE861': 'u1D1A7', 'uniE863': 'u1D1A8', 'uniE870': 'u1D1A9',
'uniE610': 'u1D1AA', 'uniE612': 'u1D1AB', 'uniE614': 'u1D1AC',
'uniE630': 'u1D1AD', 'uniE650': 'u1D1AE', 'uniE655': 'u1D1AF',
'uniE656': 'u1D1B0', 'uniE585': 'u1D1B1', 'uniE586': 'u1D1B2',
'uniE636': 'u1D1B3', 'uniE638': 'u1D1B4', 'uniE639': 'u1D1B5'}


# Get the Font
f = fl.font


# Check & decompose
print 'Checking for missing source glyphs ...'
for pua in genDict:
	if not f.has_key(pua):
		print pua + ' is missing';

print 'Checking for composites ...'
for g in f.glyphs:
	if g.name in genDict and len(g.components) > 0:
		g.Decompose()
		print 'Decomposing ' + g.name


def uIndex():
	if 'uni' in ums:
		return int(ums[3:], 16)
	else:
		return int(ums[1:], 16)


# Creating new glyphs	
print 'creating glyphs ...'
for pua, ums in genDict.iteritems():
	
	puaIndx = f.FindGlyph(pua)
	puaGlyph = f.glyphs[puaIndx]
	newGlyph = Glyph()
	newGlyph.name = ums
	newGlyph.unicode = uIndex()
	newGlyph.mark = 120
	
	if f.has_key(ums):
		print 'Skipping prexisting glyph: ' + ums
	else:
		 
#	Get components of PUA glyphs 
		newGlyph.components.append(Component(puaIndx))

# Get metrics 
		metrics = puaGlyph.GetMetrics()
		newGlyph.SetMetrics(metrics)

# Create glyphs
		f.glyphs.append(newGlyph)

fl.UpdateFont(fl.ifont)
print 'All done!'