# Rust Python Extension
Demo repo showing how to build Python extension using Rust.

### Directions

This was built using `rustc 1.4.0-nightly (dcdcc6f6b 2015-08-11)` and run on `Python 2.7.10`. To run with Python3 change the `[dependencies.cpython]` section that says `features = ["python27-sys"]` to `features = ["python3-sys"]` (note, this is untested). For best results it is recommended to use exactly what I did.

1. Run `cargo build --release`
2. Run `python try_in_python.py`

### Reason

This repo was created because my initial attempt to use the code Higgs provided didn't work due to very recent changes in [`dgrunwald/rust-cpython`](dgrunwald/rust-cpython) and [`SkylerLipthay/interpolate_idents`](https://github.com/SkylerLipthay/interpolate_idents). Long term I'm sure this will no longer be an issue but for those who want to do this now, this is helpful. Please refer to my `Cargo.toml` to see exactly what versions of these dependencies you'll need to successfully use this. NOTE: for now this repo is using a fork of `interpolate_idents` by dgrunwald, found [here](https://github.com/dgrunwald/interpolate_idents). There is a PR for these changes to be merged back in, found [here](https://github.com/SkylerLipthay/interpolate_idents/pull/1), which should hopefully soon make this repo unnecessary.

### Credit

The example code comes straight from Ewan Higgs post on using Rust cpython crate. For a more detailed look into Higgs work see his blog post [here](http://ehiggs.github.io/2015/07/Python-Modules-In-Rust/).
