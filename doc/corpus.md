# Corpus

## File format

The format for a sentence in corpus is as follows:
```
ID:  TEXT
```
With the ID being a 0-left-padded number starting at 1, separated from the
text of the sentence by a colon and two blanks.

### Groups

An empty line separates groups of sentences (e.g., on a certain theme)
within the corpus.


## Example

```
00001:  I te wā tōmua, he nui te kainga o te kekeno, te aihe, te moa.
00002:  Patua rawatia ai te moa kia ngaro rawa atu, te kekeno kia iti rawa iho.
00003:  Waihoki, ka kainga te kurī, te kiore me ngā manu iti.
00004:  Ka whakatōkia te kūmara ki ngā tahataha, kia mahana ai i te rā.
00005:  Ki te Māori he mea nui te mahi ika.
00006:  Me kī, ko te mangā ki Te Wai Pounamu, ko te tāmure ki Te Ika-a-Māui.
00007:  Ka tohu te wātaka i ngā mahi o te tau.
00008:  Ka tauhokohoko ngā hapū me ngā iwi i te kai hei aha, hei hiki mana.
00009:  Heoi, tērā ētahi ohu mahinga kai nui rawa atu.
00010:  Mō ngā hākari nui, he nui māra ka whakatōkia.

00011:  Tērā ētahi pā nui, i noho kāinga mō te hia mano tāngata.
00012:  Ko te iwi Māori te whakamutunga o ngā iwi hōpara i Te Moananui-a-Kiwa.
00013:  Hāunga te pāmamao o te whenua hou, taea noatia ai e te waka haere moana.
00014:  Taea noatia ai ngā moka o tēnei whenua mā runga waka.
00015:  Puta noa i Te Moananui-a-Kiwa, ko Tangaroa te atua o te moana.
00016:  Mō te kotahi mano tau e hī ika ana ngā iwi ki Te Moananui-a-Kiwa.
00017:  I pērā anō ngā whakamātautau i te maramataka mō te hī ika.
00018:  Ko te kiore anake o ēnei kararehe kīhai i whakarataa.
00019:  Whakaaturia ai ngā momo waka heke i Te Moananui-a-Kiwa, tae atu ki ngā whetū tātaia.
00020:  Whai anō he tino kaumoana ngā iwi tere i ēnei moana uriuri.

...
```
