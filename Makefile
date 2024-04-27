##############
# PARAMETERS #
##############
# do you want to see the commands executed ?
DO_MKDBG:=0
# do you want to check python syntax?
DO_SYNTAX:=1
# do you want to lint python files?
DO_LINT:=1
# do you want to lint python files using flake8?
DO_FLAKE8:=1
# do you want to lint python files using mypy?
DO_MYPY:=1
# do you want dependency on the Makefile itself ?
DO_ALLDEP:=1

########
# CODE #
########
# silent stuff
ifeq ($(DO_MKDBG),1)
Q:=
# we are not silent in this branch
else # DO_MKDBG
Q:=@
#.SILENT:
endif # DO_MKDBG

# dependency on the makefile itself
ifeq ($(DO_ALLDEP),1)
.EXTRA_PREREQS+=$(foreach mk, ${MAKEFILE_LIST},$(abspath ${mk}))
endif # DO_ALLDEP

ALL_PACKAGES:=$(dir $(wildcard */__init__.py))
ALL:=
ALL_PY:=$(shell find src -name "*.py")
ALL_SYNTAX:=$(addprefix out/,$(addsuffix .syntax, $(basename $(ALL_PY))))
ALL_LINT:=$(addprefix out/,$(addsuffix .lint, $(basename $(ALL_PY))))
ALL_FLAKE8:=$(addprefix out/,$(addsuffix .flake8, $(basename $(ALL_PY))))
ALL_MYPY:=$(addprefix out/,$(addsuffix .mypy, $(basename $(ALL_PY))))

ifeq ($(DO_SYNTAX),1)
ALL+=$(ALL_SYNTAX)
endif # DO_SYNTAX

ifeq ($(DO_LINT),1)
ALL+=$(ALL_LINT)
endif # DO_LINT

ifeq ($(DO_FLAKE8),1)
ALL+=$(ALL_FLAKE8)
endif # DO_FLAKE8

ifeq ($(DO_MYPY),1)
ALL+=$(ALL_MYPY)
endif # DO_MYPY

#########
# RULES #
#########
.PHONY: all
all: $(ALL)
	@true

.PHONY: install
install:
	$(info doing [$@])
	$(Q)pymakehelper symlink_install --source_folder src --target_folder ~/install/bin
	$(Q)pymakehelper symlink_install --source_folder python --target_folder ~/install/python

.PHONY: pylint
pylint:
	$(info doing [$@])
	$(Q)python -m pylint --reports=n --score=n $(ALL_PACKAGES)

.PHONY: check_shebang
check_shebang:
	$(info doing [$@])
	$(Q)head --lines=1 --quiet src/*.py | sort -u

.PHONY: debug
debug:
	$(info ALL_PY is $(ALL_PY))
	$(info ALL_SYNTAX is $(ALL_SYNTAX))
	$(info ALL_LINT is $(ALL_LINT))
	$(info ALL_FLAKE8 is $(ALL_FLAKE8))
	$(info ALL_MYPY is $(ALL_MYPY))
	$(info ALL is $(ALL))

.PHONY: clean
clean:
	$(info doing [$@])
	$(Q)rm -f $(ALL)

.PHONY: clean_hard
clean_hard:
	$(info doing [$@])
	$(Q)git clean -qffxd

.PHONY: part_flake8
part_flake8: $(ALL_FLAKE8)

.PHONY: stats
stats:
	$(Q)find out -name "*.syntax" | wc -l
	$(Q)find out -name "*.lint" | wc -l
	$(Q)find out -name "*.flake8" | wc -l
	$(Q)find out -name "*.mypy" | wc -l

############
# patterns #
############
$(ALL_SYNTAX): out/%.syntax: %.py
	$(info doing [$@])
	$(Q)pycmdtools python_check_syntax $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_LINT): out/%.lint: %.py
	$(info doing [$@])
	$(Q)PYTHONPATH=python python -m pylint --reports=n --score=n $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_FLAKE8): out/%.flake8: %.py
	$(info doing [$@])
	$(Q)python -m flake8 $<
	$(Q)pymakehelper touch_mkdir $@
$(ALL_MYPY): out/%.mypy: %.py
	$(info doing [$@])
	$(Q)pymakehelper only_print_on_error mypy $<
	$(Q)pymakehelper touch_mkdir $@
