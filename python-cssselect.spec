#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests [tests missing in archive as of 1.0.3]
#
%define		module	cssselect
Summary:	Python module for parsing CSS3 Selectors and translating them to XPath 1.0 expressions
Summary(pl.UTF-8):	Moduł Pythona interpretujący selektory CSS i tłumaczący je na wyrażenia XPath 1.0
Name:		python-%{module}
Version:	1.1.0
Release:	8
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/cssselect/
Source0:	https://files.pythonhosted.org/packages/source/c/cssselect/%{module}-%{version}.tar.gz
# Source0-md5:	fa57704c1cb66cc8e537b782bd6b227e
URL:		http://packages.python.org/cssselect/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-lxml
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cssselect parses CSS3 Selectors and translate them to XPath 1.0
expressions. Such expressions can be used in lxml or another XPath
engine to find the matching elements in an XML or HTML document. This
module used to live inside of lxml as lxml.cssselect before it was
extracted as a stand-alone project.

%description -l pl.UTF-8
cssselect interpretuje selektory CSS3 i tłumaczy je na wyrażenia XPath
1.0. Owe wyreażenia mogą być później użyte w lxml lub w innym kodzie
XPath do znajdywania pasujących elementów w dokumentach XML lub HTML.
Ten moduł był częścią lxml jako lxml.cssselect zanim został wydzielony
jako osobny projekt.

%package apidocs
Summary:	API documentation for Python cssselect module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona cssselect
Group:		Documentation

%description apidocs
API documentation for Python cssselect module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona cssselect.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%if %{with doc}
# no Makefile...
cd docs
PYTHONPATH=$(pwd)/.. \
sphinx-build -b html . _build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.rst
%{py_sitescriptdir}/cssselect
%{py_sitescriptdir}/cssselect-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
