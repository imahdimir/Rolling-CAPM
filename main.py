"""

    """

from pathlib import Path

from mirutil.ns import update_ns_module

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

class FPN :
    t0 = Path('temp-0.prq')
    t1 = Path('temp-1.prq')
    t2 = Path('temp-2.prq')
    t3 = Path('temp-3.prq')
    t4 = Path('temp-4.prq')
    t5 = Path('temp-5.prq')

class Params :
    days_2_rm_after_ipo = 40
    start_end_window = (-60 , -1)
    min_uniq_vals_in_window = 30
    model_significance_model = .05
    min_abs_abnormnal_ret = .005  # 0.5% = min abonormal return which considered as a significant one

class ColName :
    ret = c.ar1dlf + '-modified'
    w_strt_jd = "Window-Start-JDate"
    w_end_jd = "Window-End-JDate"
    w_strt_idx = "Window-Start-Index"
    w_end_idx = "Window-End-Index"
    obs = "NObs"
    nuniq = "NUniqVals"
    to_est = "to-estimate-model"
    alpha = "alpha"
    alpha_std = "alpha-std"
    alpha_t = "alpha-t"
    alpha_p = "alpha-p"
    beta = "beta"
    beta_std = "beta-std"
    beta_t = "beta-t"
    beta_p = "beta-p"
    f_stat = "F-stat"
    f_p = "F-p"
    r2 = "R2"
    r2_adj = "R2-adj"
    dw = "DW"
    cred_model = 'is-Credible-Model'
    expctd_exss_ret = 'Expected-Excess-Return'
    abnrml_ret = 'Abnormal-Return'
    is_abnrml_ret_signfcnt = 'Is-Abnormal-Return-Significant'

def main() :
    pass

    ##

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')

##


# noinspection PyUnreachableCode
if False :
    pass

    ##

    ##
