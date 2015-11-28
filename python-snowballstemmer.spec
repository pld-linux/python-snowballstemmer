#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	snowballstemmer
Summary:	Stemmer algorithms generated from Snowball algorithms
Summary(pl.UTF-8):	Algorytmy wyznaczające rdzeniesłów wygenerowane z algorytmów Snowball
Name:		python-%{module}
Version:	1.2.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/snowballstemmer
Source0:	https://pypi.python.org/packages/source/s/snowballstemmer/%{module}-%{version}.tar.gz
# Source0-md5:	51f2ef829db8129dd0f2354f0b209970
URL:		https://github.com/shibukawa/snowball_py
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides 16 stemmer algorithms (15 + Porter English
stemmer) generated from Snowball algorithms.

It includes following language algorithms:
 - Danish
 - Dutch
 - English (Standard, Porter)
 - Finnish
 - French
 - German
 - Hungarian
 - Italian
 - Norwegian
 - Portuguese
 - Romanian
 - Russian
 - Spanish
 - Swedish
 - Turkish

This is a pure Python stemming library. If PyStemmer is available,
this module uses it to accelerate.

%description -l pl.UTF-8
Ten pakiet udostępnia 16 algorytmów znajdujących rdzenie słów (15 +
angielski Portera), wygenerowane z algorytmów Snowball.

Zawiera algorytmy dla następujących języków:
 - duński
 - holenderski
 - angielski (standardowy i Portera)
 - fiński
 - francuski
 - niemiecki
 - węgierski
 - włoski
 - norweski
 - portugalski
 - rumuński
 - rosyjski
 - hiszpański
 - szwedzki
 - turecki

Ta biblioteka jest napisana w czystym Pythonie. Jeśli dostępny jest
PyStemmer, jest używany w celu przyspieszenia.

%package -n python3-%{module}
Summary:	Stemmer algorithms generated from Snowball algorithms
Summary(pl.UTF-8):	Algorytmy wyznaczające rdzeniesłów wygenerowane z algorytmów Snowball
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This package provides 16 stemmer algorithms (15 + Porter English
stemmer) generated from Snowball algorithms.

It includes following language algorithms:

 - Danish
 - Dutch
 - English (Standard, Porter)
 - Finnish
 - French
 - German
 - Hungarian
 - Italian
 - Norwegian
 - Portuguese
 - Romanian
 - Russian
 - Spanish
 - Swedish
 - Turkish

This is a pure Python stemming library. If PyStemmer is available,
this module uses it to accelerate.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet udostępnia 16 algorytmów znajdujących rdzenie słów (15 +
angielski Portera), wygenerowane z algorytmów Snowball.

Zawiera algorytmy dla następujących języków:
 - duński
 - holenderski
 - angielski (standardowy i Portera)
 - fiński
 - francuski
 - niemiecki
 - węgierski
 - włoski
 - norweski
 - portugalski
 - rumuński
 - rosyjski
 - hiszpański
 - szwedzki
 - turecki

Ta biblioteka jest napisana w czystym Pythonie. Jeśli dostępny jest
PyStemmer, jest używany w celu przyspieszenia.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
