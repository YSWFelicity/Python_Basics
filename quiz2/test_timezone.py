from timezone import est_to_pst


def test_est_to_pst():
    assert(est_to_pst("07:34") == "04:34")
    assert(est_to_pst("08:34") == "05:34")
    assert(est_to_pst("13:34") == "10:34")
