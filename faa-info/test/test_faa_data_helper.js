'use strict';
var chai = require('chai');
var chaiAsPromised = require('chai-as-promised');
chai.use(chaiAsPromised);
var expect = chai.expect;
var FAADataHelper = require('../faa_data_helper');
chai.config.includeStack = true;

describe('FAADataHelper', function() {
  var subject = new FAADataHelper();
  var airport_code;
  describe('#getAirportStatus', function() {
    context('with an invalid airport code', function() {
      it('returns an error', function() {
        airport_code = 'PUNKYBREWSTER';
        return expect(subject.requestAirportStatus(airport_code)).to.be.rejectedWith(Error);
      });
    });
    context('with a valid airport code', function() {
      it('returns matching airport code', function() {
        airport_code = 'SFO';
        var value = subject.requestAirportStatus(airport_code).then(function(obj) {
          return obj.IATA;
        });
        /*
        This is a special part of the chai-as-promised matcher we added, which allows us to make assertions about the data a Promise returns without requiring the use of callbacks, “sleeps” or other less-than-ideal approaches to waiting for the request to complete.
        */
        return expect(value).to.eventually.eq(airport_code);
      });
    });
  });
});
