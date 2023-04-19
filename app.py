from flask import Flask, request
from beem import Steem


app = Flask(__name__)
steem = Steem("https://api.steemit.com")

@app.route('/sp_to_sbd')
def sp_to_sbd():
    _sp = float(request.args.get('sp'))
    _prs = int(request.args.get('prs'))
    _vp = int(request.args.get('vp'))
    _pct = int(request.args.get('pct'))

    val = steem.sp_to_sbd(_sp, _prs, _vp, _pct, not_broadcasted_vote=True)

    return str(val)

@app.route('/sbd_to_vote_pct')
def sbd_to_vote_pct():
    _sbd = request.args.get('sbd')
    _prs = float(request.args.get('prs'))
    _sp = float(request.args.get('sp'))
    _vp = float(request.args.get('vp'))
    _sbd = _sbd + " SBD"

    perc = steem.sbd_to_vote_pct(sbd=_sbd, post_rshares=_prs, steem_power=_sp, vests=None, voting_power=_vp, not_broadcasted_vote=True, use_stored_data=True)

    return str(perc)

if __name__ == '__main__':
    app.run()