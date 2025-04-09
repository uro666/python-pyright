%define module pyright
# disable tests on abf
%bcond_with test

Name:		python-pyright
Version:	1.1.398
Release:	1
Summary:	Command line wrapper for pyright
URL:		https://pypi.org/project/pyright/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pyright/pyright-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(nodeenv)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pluggy)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-subprocess)
BuildRequires:	python%{pyver}dist(ruff)
BuildRequires:	python%{pyver}dist(twine)
%endif
Requires:	python%{pyver}dist(nodeenv) >= 1.6.0
Requires:	python%{pyver}dist(typing-extensions) >= 4.1


%description
Command line wrapper for pyright

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
# ignore tests that require internet access
%{__python} -m pytest --import-mode append -v tests/ \
--ignore tests/test_main.py \
--ignore tests/test_langserver.py \
--ignore tests/test_node.py
%endif

%files
%{_bindir}/pyright
%{_bindir}/pyright-python
%{_bindir}/pyright-langserver
%{_bindir}/pyright-python-langserver
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.md
