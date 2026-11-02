"""Prevent later refreshes and old rebuilds from duplicating source revisions."""
import importlib.util,json,sys
from pathlib import Path
import pytest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import research_revisions as revisions


@pytest.fixture
def revised_row(tmp_path,monkeypatch):
    monkeypatch.setattr(revisions,'ROOT',tmp_path)
    prior={'poll_id':'fl_gov--survey','race_id':'fl_gov','sample_id':'same-wave','independent_b':.55}
    path=tmp_path/'research/baseline.json';path.parent.mkdir();path.write_text(json.dumps({'polls':[prior]}))
    current={**prior,'independent_b':.56,'supersedes_record':{'baseline_path':'research/baseline.json','sha256':revisions.digest(prior)}}
    return prior,current,path


def test_older_rebuild_preserves_revision_and_pins_original(revised_row):
    prior,current,_=revised_row
    assert revisions.apply_current_revisions([prior],[current])==[current]
    assert revisions.original_rows([current])==[prior]
    assert not revisions.same_race_inputs([current],[prior],'fl_gov')


def test_revision_rejects_changed_predecessor_archive(revised_row):
    _,current,path=revised_row
    content=json.loads(path.read_text());content['polls'][0]['independent_b']=.54
    path.write_text(json.dumps(content))
    with pytest.raises(ValueError,match='hash mismatch'):revisions.original_row(current)


def test_revision_cannot_replace_a_different_survey(revised_row):
    prior,current,_=revised_row
    with pytest.raises(ValueError,match='same race and survey'):
        revisions.original_row({**current,'sample_id':'different-wave'})
    with pytest.raises(ValueError,match='differs from revision predecessor'):
        revisions.apply_current_revisions([{**prior,'independent_b':.54}],[current])
