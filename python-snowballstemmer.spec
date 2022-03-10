#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	snowballstemmer
Summary:	Stemmer algorithms generated from Snowball algorithms
Summary(pl.UTF-8):	Algorytmy wyznaczające rdzeniesłów wygenerowane z algorytmów Snowball
Name:		python-%{module}
Version:	2.2.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/snowballstemmer
Source0:	https://files.pythonhosted.org/packages/source/s/snowballstemmer/%{module}-%{version}.tar.gz
# Source0-md5:	4332ddc7bbee0f344a03915b2ad59a54
URL:		https://github.com/snowballstem/snowball
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides 26 stemmer algorithms (25 languages + Porter
English stemmer) generated from Snowball algorithms.

It includes following language algorithms:
 - Arabic
 - Basque
 - Catalan
 - Danish
 - Dutch
 - English (Standard, Porter)
 - Finnish
 - French
 - German
 - Greek
 - Hindi
 - Hungarian
 - Indonesian
 - Irish
 - Italian
 - Lithuanian
 - Nepali
 - Norwegian
 - Portuguese
 - Romanian
 - Russian
 - Spanish
 - Swedish
 - Tamil
 - Turkish

This is a pure Python stemming library. If PyStemmer is available,
this module uses it to accelerate.

%description -l pl.UTF-8
Ten pakiet udostępnia 26 algorytmów znajdujących rdzenie słów (25
języków + angielski Portera), wygenerowane z algorytmów Snowball.

Zawiera algorytmy dla następujących języków:
 - arabski
 - baskijski
 - kataloński
 - duński
 - holenderski
 - angielski (standardowy i Portera)
 - fiński
 - francuski
 - niemiecki
 - grecki
 - hindi
 - węgierski
 - indonezyjski
 - irlandzki
 - włoski
 - litewski
 - nepalski
 - norweski
 - portugalski
 - rumuński
 - rosyjski
 - hiszpański
 - szwedzki
 - tamilski
 - turecki

Ta biblioteka jest napisana w czystym Pythonie. Jeśli dostępny jest
PyStemmer, jest używany w celu przyspieszenia.

%package -n python3-%{module}
Summary:	Stemmer algorithms generated from Snowball algorithms
Summary(pl.UTF-8):	Algorytmy wyznaczające rdzeniesłów wygenerowane z algorytmów Snowball
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This package provides 26 stemmer algorithms (25 languages + Porter
English stemmer) generated from Snowball algorithms.

It includes following language algorithms:
 - Arabic
 - Basque
 - Catalan
 - Danish
 - Dutch
 - English (Standard, Porter)
 - Finnish
 - French
 - German
 - Greek
 - Hindi
 - Hungarian
 - Indonesian
 - Irish
 - Italian
 - Lithuanian
 - Nepali
 - Norwegian
 - Portuguese
 - Romanian
 - Russian
 - Spanish
 - Swedish
 - Tamil
 - Turkish

This is a pure Python stemming library. If PyStemmer is available,
this module uses it to accelerate.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet udostępnia 26 algorytmów znajdujących rdzenie słów (25
języków + angielski Portera), wygenerowane z algorytmów Snowball.

Zawiera algorytmy dla następujących języków:
 - arabski
 - baskijski
 - kataloński
 - duński
 - holenderski
 - angielski (standardowy i Portera)
 - fiński
 - francuski
 - niemiecki
 - grecki
 - hindi
 - węgierski
 - indonezyjski
 - irlandzki
 - włoski
 - litewski
 - nepalski
 - norweski
 - portugalski
 - rumuński
 - rosyjski
 - hiszpański
 - szwedzki
 - tamilski
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
%doc COPYING NEWS README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc COPYING NEWS README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
