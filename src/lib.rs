#![feature(plugin)]
#![plugin(interpolate_idents)]

#[macro_use] extern crate cpython;

use cpython::{PyResult, Python, PyTuple, PyDict, PyErr, exc, ToPyObject, PythonObject};

mod fib {

    pub fn fib(n : u64) -> u64 {
        if n < 2 {
            return 1
        }
        let mut prev1 = 1;
        let mut prev2 = 1;
        for _ in 1..n {
            let new = prev1 + prev2;
            prev2 = prev1;
            prev1 = new;
        }
        prev1
    }
}

py_module_initializer!(librust_python_example, |_py, m| {
    try!(m.add("__doc__", "Calculates fib number in rust"));
    try!(m.add("fib", py_fn!(fib)));
    Ok(())
});

fn fib<'p>(py: Python<'p>, args: &PyTuple<'p>, kwargs: Option<&PyDict<'p>>) -> PyResult<'p, u64> {
    let arg0 = match args.get_item(0).extract::<u64>() {
        Ok(x) => x,
        Err(_) => {
            let msg = "Fib takes a number greater than 0";
            let pyerr = PyErr::new_lazy_init(py.get_type::<exc::ValueError>(), Some(msg.to_py_object(py).into_object()));
            return Err(pyerr);
        }
    };
    Ok(fib::fib(arg0))
}
