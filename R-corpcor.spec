#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-corpcor
Version  : 1.6.9
Release  : 5
URL      : https://cran.r-project.org/src/contrib/corpcor_1.6.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/corpcor_1.6.9.tar.gz
Summary  : Efficient Estimation of Covariance and (Partial) Correlation
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : clr-R-helpers

%description
the covariance matrix, with separate shrinkage for variances and correlations.  
  The details of the method are explained in Schafer and Strimmer (2005)

%prep
%setup -q -c -n corpcor

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523296124

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523296124
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corpcor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corpcor
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library corpcor
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library corpcor|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/corpcor/DESCRIPTION
/usr/lib64/R/library/corpcor/INDEX
/usr/lib64/R/library/corpcor/Meta/Rd.rds
/usr/lib64/R/library/corpcor/Meta/features.rds
/usr/lib64/R/library/corpcor/Meta/hsearch.rds
/usr/lib64/R/library/corpcor/Meta/links.rds
/usr/lib64/R/library/corpcor/Meta/nsInfo.rds
/usr/lib64/R/library/corpcor/Meta/package.rds
/usr/lib64/R/library/corpcor/NAMESPACE
/usr/lib64/R/library/corpcor/NEWS
/usr/lib64/R/library/corpcor/R/corpcor
/usr/lib64/R/library/corpcor/R/corpcor.rdb
/usr/lib64/R/library/corpcor/R/corpcor.rdx
/usr/lib64/R/library/corpcor/help/AnIndex
/usr/lib64/R/library/corpcor/help/aliases.rds
/usr/lib64/R/library/corpcor/help/corpcor.rdb
/usr/lib64/R/library/corpcor/help/corpcor.rdx
/usr/lib64/R/library/corpcor/help/paths.rds
/usr/lib64/R/library/corpcor/html/00Index.html
/usr/lib64/R/library/corpcor/html/R.css
