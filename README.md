## pyephemapi

An incredibly tiny project to make a REST API for
[PyEphem](http://rhodesmill.org/pyephem/) so that you can do
TLE to satellite position but not write your own server or think
too much.

### example

```js
var tle =     [
  'WORLDVIEW-1 (WV-1)',
  '1 32060U 07041A   13222.53694131  .00003301  00000-0  13725-3 0  5540',
  '2 32060  97.3385 296.1673 0001236 108.0040   5.4207 15.24471932327959'
];

d3.json('http://ephemapi.herokuapp.com/?name=' + encodeURIComponent(tle[0]) +
    '&line1=' + encodeURIComponent(tle[1]) +
    '&line2=' + encodeURIComponent(tle[2])).on('load', function(data) {
        cb(data);
    }).get();
    
// data is
{
  "coords": [
    0.05179675295948982, 
    -0.5329474210739136
  ]
}
```
